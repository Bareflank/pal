from pal.writer.print_mechanism.print_mechanism import PrintMechanismWriter


class NonePrintMechanismWriter(PrintMechanismWriter):

    def print_value_as_register(self, outfile, register, value):
        pass

    def print_value_as_field(self, outfile, register, field, value):
        pass
