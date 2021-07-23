import os
import pathlib

from pal.generator.abstract_generator import AbstractGenerator
from pal.logger import logger
from pal.exception import PalGeneratorException
from pal.filter import filters
from pal.transform import transforms


class RustGenerator(AbstractGenerator):
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
            regs = filters["irregular_size"].filter_exclusive(regs)

            logger.info("Generating Rust register accessors to: " + str(outpath))

            for reg in regs:
                outfile_path = os.path.join(outpath, reg.name.lower() + ".rs")
                outfile_path = os.path.abspath(outfile_path)

                with open(outfile_path, "w") as outfile:
                    self._generate_register(outfile, reg)

            self.__update_module_files(outpath)
            self.__update_lib_file(outpath)


        except Exception as e:
            msg = "{g} failed to generate output {out}: {exception}".format(
                g=str(type(self).__name__),
                out=outpath,
                exception=e)
            raise PalGeneratorException(msg)

    def generate_instructions(self, instructions, outpath):
        try:
            logger.info("Generating Rust instruction accessors to: " + str(outpath))

            for inst in instructions:

                outfile_path = os.path.join(outpath, inst.name.lower() + ".rs")
                outfile_path = os.path.abspath(outfile_path)

                with open(outfile_path, "w") as outfile:
                    self._generate_instruction(outfile, inst)

            self.__update_module_files(outpath)
            self.__update_lib_file(outpath)

        except Exception as e:
            msg = "{g} failed to generate output {out}: {exception}".format(
                g=str(type(self).__name__),
                out=outpath,
                exception=e)
            raise PalGeneratorException(msg)

    def _generate_register(self, outfile, reg):

        self.writer.declare_register_dependencies(outfile, reg, self.config)
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

    def __update_module_files(self, outpath):
        modfile_path = os.path.join(outpath, "mod.rs")
        modfile_path = os.path.abspath(modfile_path)

        for root, dirs, files in os.walk(outpath):
            logger.info("Updating modfile: " + os.path.join(root, "mod.rs"))
            with open(os.path.join(root, "mod.rs"), "w") as modfile:
                for name in sorted(files):
                    if name != "mod.rs" and name.endswith(".rs"):
                        modname = os.path.splitext(name)[0]
                        modfile.write("pub mod " + modname + ";")
                        self.writer.write_newline(modfile)
                        modfile.write("pub use " + modname + "::*;")
                        self.writer.write_newline(modfile)

                for name in sorted(dirs):
                    modname = os.path.splitext(name)[0]
                    modfile.write("pub mod " + modname + ";")
                    self.writer.write_newline(modfile)
                    modfile.write("pub use " + modname + "::*;")
                    self.writer.write_newline(modfile)

    def __update_lib_file(self, outpath):
        libfile_path = os.path.abspath(os.path.join(outpath, "lib.rs"))
        libfile_dir = os.path.abspath(outpath)

        if not os.path.exists(libfile_path):
            libfile_path = os.path.abspath(os.path.join(outpath, "../lib.rs"))
            libfile_dir = os.path.abspath(os.path.join(outpath, "../"))
            if not os.path.exists(libfile_path):
                return

        logger.info("Updating lib.rs: " + str(libfile_path))

        with open(libfile_path, "w") as libfile:
            #  libfile.write("pub mod pal {")
            #  self.writer.write_newline(libfile)

            for child in [f.path for f in os.scandir(libfile_dir)]:
                logger.info("child: " + str(child))
                modname = os.path.splitext(os.path.basename(child))[0]
                if not modname == "lib":
                    libfile.write("pub mod " + modname + ";")
                    self.writer.write_newline(libfile)

            #  libfile.write("}")
