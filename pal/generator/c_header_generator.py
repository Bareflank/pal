import os

from pal.generator.abstract_generator import AbstractGenerator
from pal.logger import logger
from pal.config import config
from pal.exception import PalGeneratorException
from pal.filter import filters
from pal.transform import transforms
import pal.gadget


class CHeaderGenerator(AbstractGenerator):
    def generate_registers(self, regs, outpath):
        try:
            regs = transforms["remove_reserved_0"].transform(regs)
            regs = transforms["remove_reserved_1"].transform(regs)
            regs = transforms["remove_reserved_sign_extended"].transform(regs)
            regs = transforms["remove_implementation_defined"].transform(regs)
            regs = transforms["special_to_underscore"].transform(regs)
            regs = transforms["insert_valid_first_character"].transform(regs)
            regs = transforms["remove_redundant_am"].transform(regs)
            regs = transforms["remove_redundant_fields"].transform(regs)
            regs = transforms["unique_fieldset_names"].transform(regs)

            regs = filters["no_access_mechanism"].filter_exclusive(regs)

            logger.info("Generating C header file registers to: " + str(outpath))

            for reg in regs:
                include_guard = "PAL_" + reg.name.upper() + "_H"
                self.gadgets["pal.include_guard"].name = include_guard

                outfile_path = os.path.join(outpath, reg.name.lower() + ".h")
                outfile_path = os.path.abspath(outfile_path)

                with open(outfile_path, "w") as outfile:
                    self._generate_register(outfile, reg)

        except Exception as e:
            msg = "{g} failed to generate output {out}: {exception}".format(
                g=str(type(self).__name__),
                out=outpath,
                exception=e)
            raise PalGeneratorException(msg)

    def generate_instructions(self, instructions, outpath):
        try:
            logger.info("Generating C header file instructions to: " + str(outpath))

            for inst in instructions:
                include_guard = "PAL_EXECUTE_" + inst.name.upper() + "_H"
                self.gadgets["pal.include_guard"].name = include_guard

                outfile_path = os.path.join(outpath, inst.name.lower() + ".h")
                outfile_path = os.path.abspath(outfile_path)

                with open(outfile_path, "w") as outfile:
                    self._generate_instruction(outfile, inst)

        except Exception as e:
            msg = "{g} failed to generate output {out}: {exception}".format(
                g=str(type(self).__name__),
                out=outpath,
                exception=e)
            raise PalGeneratorException(msg)

    @pal.gadget.license
    @pal.gadget.include_guard
    def _generate_register(self, outfile, reg):

        self.writer.declare_register_dependencies(outfile, reg)
        self.writer.declare_print_mechanism_dependencies(outfile, reg)

        for am_key, am_list in reg.access_mechanisms.items():
            for am in am_list:
                self.writer.declare_access_mechanism_dependencies(outfile, reg, am)

        self.writer.write_newline(outfile)

        self._generate_register_comment(outfile, reg)
        self.writer.declare_register_accessors(outfile, reg)

        for idx, fieldset in enumerate(reg.fieldsets):
            if fieldset.condition:
                self.writer.declare_comment(outfile, fieldset.condition, 79)

            for field in fieldset.fields:
                self.writer.declare_field_accessors(outfile, reg, field)
                self.writer.declare_field_printers(outfile, reg, field)

            if reg.is_readable():
                self.writer.declare_fieldset_printers(outfile, reg, fieldset)

    @pal.gadget.license
    @pal.gadget.include_guard
    def _generate_instruction(self, outfile, inst):
        self.writer.declare_instruction_dependencies(outfile, inst)
        self.writer.declare_instruction_accessor(outfile, inst)
        self.writer.write_newline(outfile)

    def _generate_register_comment(self, outfile, reg):
        comment = "{name} ({long_name}){separator}{purpose}".format(
            name=str(reg.name),
            long_name=str(reg.long_name),
            separator=" - " if reg.purpose else "",
            purpose=str(reg.purpose)
        )
        self.writer.declare_comment(outfile, comment, 75)
