from pal.writer.register.register import RegisterWriter


class NoneRegisterWriter(RegisterWriter):

    def declare_register_dependencies(self, outfile, register, config):
        pass

    def declare_register_accessors(self, outfile, register):
        pass

    def declare_field_accessors(self, outfile, register, field):
        pass

    def call_register_get(self, outfile, register, destination, index="index"):
        pass

    def call_field_get(self, outfile, register, field, destination,
                       register_value):
        pass

    def declare_field_printers(self, outfile, register, field):
        pass

    def declare_fieldset_printers(self, outfile, register, fieldset):
        pass
