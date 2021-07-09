import textwrap
from pal.writer.register.register import RegisterWriter


class YamlRegisterWriter(RegisterWriter):

    def declare_register_dependencies(self, outfile, register, config):
        pass

    def declare_register_accessors(self, outfile, register):
        self._declare_register_constants(outfile, register)

    def declare_field_accessors(self, outfile, register, field):
        self._declare_field_constants(outfile, register, field)

    def declare_field_printers(outfile, register, field):
        pass

    def declare_fieldset_printers(outfile, register, fieldset):
        pass

    def call_register_get(self, outfile, register, destination, index="index"):
        pass

    def call_field_get(self, outfile, register, field, destination,
                       register_value):
        pass

    # -------------------------------------------------------------------------
    # private
    # -------------------------------------------------------------------------
    def _declare_register_constants(self, outfile, register):
        outfile.write("- name: " + str(register.name))
        self.write_newline(outfile)

        if register.long_name:
            self.write_indent(outfile)
            outfile.write("long_name: \"" + str(register.long_name) + "\"")
            self.write_newline(outfile)

        if register.purpose:
            self.write_indent(outfile)
            outfile.write("purpose: |")
            self.write_newline(outfile)

            self.write_indent(outfile, count=2)
            outfile.write("\"")
            self.write_newline(outfile)

            wrapped = textwrap.wrap(str(register.purpose), width=72)
            for line in wrapped:
                self.write_indent(outfile, count=2)
                outfile.write(str(line))
                self.write_newline(outfile)

            self.write_indent(outfile, count=2)
            outfile.write("\"")
            self.write_newline(outfile)

        self.write_indent(outfile)
        outfile.write("size: " + str(register.size))
        self.write_newline(outfile)

        self.write_indent(outfile)
        outfile.write("arch: " + str(register.arch))
        self.write_newline(outfile)

        if register.is_internal:
            self.write_indent(outfile)
            outfile.write("is_internal: True")
            self.write_newline(outfile)

        if register.is_optional:
            self.write_indent(outfile)
            outfile.write("is_optional: True")
            self.write_newline(outfile)

        if register.arch == "armv8-a":
            self.write_indent(outfile)
            outfile.write("execution_state: " + str(register.execution_state))
            self.write_newline(outfile)

            if register.is_banked:
                self.write_indent(outfile)
                outfile.write("is_banked: True")
                self.write_newline(outfile)

        self.write_newline(outfile)

    def _declare_field_constants(self, outfile, register, field):
        self.write_indent(outfile, count=5)
        outfile.write("- name: " + str(field.name))
        self.write_newline(outfile)

        if field.long_name:
            self.write_indent(outfile, count=6)
            outfile.write("long_name: \"" + str(field.long_name) + "\"")
            self.write_newline(outfile)

        self.write_indent(outfile, count=6)
        outfile.write("lsb: " + str(field.lsb))
        self.write_newline(outfile)

        self.write_indent(outfile, count=6)
        outfile.write("msb: " + str(field.msb))
        self.write_newline(outfile)

        if field.description:
            self.write_indent(outfile, count=6)
            outfile.write("description: \"" + str(field.long_name) + "\"")
            self.write_newline(outfile)

        if field.readable:
            self.write_indent(outfile, count=6)
            outfile.write("readable: True")
            self.write_newline(outfile)

        if field.writable:
            self.write_indent(outfile, count=6)
            outfile.write("writable: True")
            self.write_newline(outfile)

        if field.lockable:
            self.write_indent(outfile, count=6)
            outfile.write("lockable: True")
            self.write_newline(outfile)

        if field.write_once:
            self.write_indent(outfile, count=6)
            outfile.write("write_once: True")
            self.write_newline(outfile)

        if field.write_1_clear:
            self.write_indent(outfile, count=6)
            outfile.write("write_1_clear: True")
            self.write_newline(outfile)

        if field.reserved0:
            self.write_indent(outfile, count=6)
            outfile.write("reserved0: True")
            self.write_newline(outfile)

        if field.reserved1:
            self.write_indent(outfile, count=6)
            outfile.write("reserved1: True")
            self.write_newline(outfile)

        if field.preserved:
            self.write_indent(outfile, count=6)
            outfile.write("preserved: True")
            self.write_newline(outfile)
