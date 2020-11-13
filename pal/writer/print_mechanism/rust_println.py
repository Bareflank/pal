from pal.writer.print_mechanism.print_mechanism import PrintMechanismWriter


class RustPrintlnPrintMechanismWriter(PrintMechanismWriter):

    def declare_print_mechanism_dependencies(self, outfile, register):
        pass

    def print_value_as_register(self, outfile, register, value):
        outfile.write('println!("TODO: Make me printable!");')
        self.write_newline(outfile)

    def print_value_as_field(self, outfile, register, field, value):
        outfile.write('println!("TODO: Make me printable!");')
        self.write_newline(outfile)
