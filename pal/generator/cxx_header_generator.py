import os

import pal.gadget
from pal.generator.abstract_generator import AbstractGenerator
from pal.logger import logger
from pal.config import config
from pal.filter import filters
from pal.transform import transforms
from pal.exception import PalGeneratorException
from pal.writer.writer_factory import make_writer


class CxxHeaderGenerator(AbstractGenerator):

    def generate(self, regs, outpath):
        try:
            regs = filters["no_access_mechanism"].filter_exclusive(regs)
            regs = transforms["remove_reserved_0"].transform(regs)
            regs = transforms["remove_reserved_1"].transform(regs)
            regs = transforms["remove_preserved"].transform(regs)
            regs = transforms["special_to_underscore"].transform(regs)

            logger.info("Generating outputs to: " + str(outpath))

            for reg in regs:
                include_guard = "PAL_" + reg.name.upper() + "_H"
                self.gadgets["pal.include_guard"].name = include_guard
                self.gadgets["pal.header_depends"].includes = [
                    "<stdint.h>"
                ]

                outfile_path = os.path.join(outpath, reg.name.lower() + ".h")
                outfile_path = os.path.abspath(outfile_path)

                with open(outfile_path, "w") as outfile:
                    self.gadgets["pal.cxx.namespace"].name = "pal"
                    self._generate_register(outfile, reg)

            self.gadgets["pal.cxx.namespace"].indent_contents = False

        except Exception as e:
            msg = "{g} failed to generate output {out}: {exception}".format(
                g=str(type(self).__name__),
                out=outpath,
                exception=e)
            raise PalGeneratorException(msg)

    # -------------------------------------------------------------------------
    # private
    # -------------------------------------------------------------------------

    @pal.gadget.license
    @pal.gadget.include_guard
    @pal.gadget.header_depends
    @pal.gadget.cxx.namespace
    def _generate_register(self, outfile, reg):
        self.writer.write_newline(outfile)
        self._generate_register_comment(outfile, reg)

        self.gadgets["pal.cxx.namespace"].name = reg.name.lower()
        self.gadgets["pal.cxx.namespace"].indent_contents = True
        self._generate_register_accessors(outfile, reg)

    def _generate_register_comment(self, outfile, reg):
        comment = "{name} ({long_name}){separator}{purpose}".format(
            name=str(reg.name),
            long_name=str(reg.long_name),
            separator=" - " if reg.purpose else "",
            purpose=str(reg.purpose)
        )
        self.writer.declare_comment(outfile, comment, wrap=75)

    @pal.gadget.cxx.namespace
    def _generate_register_accessors(self, outfile, reg):
        self.writer.declare_register_constants(outfile, reg)
        self.writer.declare_access_mechanism_dependencies(outfile, reg)

        if reg.is_readable():
            self.writer.declare_register_get(outfile, reg)
        if reg.is_writeable():
            self.writer.declare_register_set(outfile, reg)
        fieldsets = reg.fieldsets

        for idx, fieldset in enumerate(fieldsets):
            if len(fieldsets) > 1:
                self.writer.declare_comment(outfile, fieldset.condition)
                self.gadgets["pal.cxx.namespace"].name = "fieldset_" + str(idx + 1)
                self._generate_fieldset_in_namespace(outfile, reg, fieldsets[0])
            else:
                self._generate_fieldset(outfile, reg, fieldsets[0])

    @pal.gadget.cxx.namespace
    def _generate_fieldset_in_namespace(self, outfile, reg, fieldset):
        self._generate_fieldset(outfile, reg, fieldset)

    def _generate_fieldset(self, outfile, reg, fieldset):
        for idx, field in enumerate(fieldset.fields):
            if field.description:
                self.writer.declare_comment(outfile, field.description, wrap=71)

            self.gadgets["pal.cxx.namespace"].name = field.name.lower()
            self._generate_register_field(outfile, reg, field)
            self.writer.write_newline(outfile)

        if reg.is_readable():
            self.writer.declare_fieldset_printer(outfile, reg, fieldset)

    @pal.gadget.cxx.namespace
    def _generate_register_field(self, outfile, reg, field):
        self.writer.declare_field_constants(outfile, reg, field)
        self.writer.declare_field_accessors(outfile, reg, field)
        self.writer.declare_field_printer(outfile, reg, field)
