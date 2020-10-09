import os

from pal.generator.abstract_generator import AbstractGenerator
from pal.exception import PalGeneratorException


class YamlDataGenerator(AbstractGenerator):
    def generate_registers(self, regs, outpath):
        try:
            for reg in regs:
                outfile = reg.name.lower() + ".yml"
                outfile_path = os.path.abspath(os.path.join(outpath, outfile))
                with open(outfile_path, "w") as outfile:
                    self._generate(outfile, reg)

        except Exception as e:
            msg = "{g} failed to generate output {out}: {exception}".format(
                g=str(type(self).__name__),
                out=outpath,
                exception=e)
            raise PalGeneratorException(msg)

    def generate_instructions(self, instructions, outpath):
        # TODO: Implement YAML instruction generation
        pass

    def _generate(self, outfile, reg):
        self.writer.declare_register_accessors(outfile, reg)
        self.writer.declare_register_accessors(outfile, reg)
        self._generate_register_fieldsets(outfile, reg)

    def _generate_register_fieldsets(self, outfile, reg):
        if not reg.fieldsets:
            return

        self.writer.write_indent(outfile)
        outfile.write("fieldsets:")
        self.writer.write_newline(outfile)

        for idx, fs in enumerate(reg.fieldsets):
            self.writer.write_indent(outfile, count=3)
            if fs.name:
                outfile.write("- name: " + str(fs.name))
                self.writer.write_newline(outfile)
            else:
                outfile.write("- name: " + "fieldset_" + str(idx + 1))
                self.writer.write_newline(outfile)

            if fs.condition:
                self.writer.write_indent(outfile, count=4)
                outfile.write("condition: \"" + str(fs.condition) + "\"")
                self.writer.write_newline(outfile)

            if fs.size:
                self.writer.write_indent(outfile, count=4)
                outfile.write("size: " + str(fs.size))
                self.writer.write_newline(outfile)

            self.writer.write_newline(outfile)

            self._generate_fields(outfile, reg, fs)

            if idx != len(reg.fieldsets) - 1:
                outfile.write("\n")

    def _generate_fields(self, outfile, reg, fs):
        self.writer.write_indent(outfile, count=4)
        outfile.write("fields:\n")
        for idx, f in enumerate(fs.fields):
            self.writer.declare_field_accessors(outfile, reg, f)

            if idx != len(fs.fields) - 1:
                self.writer.write_newline(outfile)
