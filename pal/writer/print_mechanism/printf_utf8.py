from pal.writer.print_mechanism.print_mechanism import PrintMechanismWriter


class PrintfUtf8PrintMechanismWriter(PrintMechanismWriter):

    def declare_print_mechanism_dependencies(self, outfile, register):
        outfile.write("#include <stdio.h>")
        self.write_newline(outfile)
        outfile.write("#include <inttypes.h>")
        self.write_newline(outfile)

    def print_value_as_register(self, outfile, register, value):
        hex_format = self._get_hex_format_string(register.size)
        outfile.write('printf("' + hex_format + ' ", ')
        outfile.write(str(value) + ');')
        self.write_newline(outfile)

        outfile.write('printf("%s ", "' + str(register.name) + '");')
        self.write_newline(outfile)

        if register.long_name:
            outfile.write('printf("(%s)", "' + str(register.long_name) + '");')
            self.write_newline(outfile)

        outfile.write('printf("\\n");')
        self.write_newline(outfile)

    def print_value_as_field(self, outfile, register, field, value):
        outfile.write('printf("    ");')
        self.write_newline(outfile)

        outfile.write('printf("[%02u:%02u] ", ')
        outfile.write(str(field.msb) + ', ')
        outfile.write(str(field.lsb) + ');')
        self.write_newline(outfile)

        if field.msb == field.lsb:
            outfile.write('printf("%-16s", "");')
            self.write_newline(outfile)

            outfile.write('printf("%s", ')
            outfile.write(str(value) + ' ? ')
            outfile.write('"\\033[1;32m \\xE2\\x9C\\x93 \\033[0m" : ')
            outfile.write('"\\033[1;31m \\xE2\\x9C\\x97 \\033[0m"')
            outfile.write(');')
            self.write_newline(outfile)

        else:
            hex_format = self._get_hex_format_string(register.size)
            outfile.write('printf("' + hex_format + ' ", ')
            outfile.write(str(value))
            outfile.write(');')
            self.write_newline(outfile)

        outfile.write('printf("%-20s", "')
        outfile.write(str(field.name) + '");')
        self.write_newline(outfile)

        if field.long_name != field.name:
            outfile.write('printf("(%s)", "' + str(field.long_name) + '");')
            self.write_newline(outfile)

        outfile.write('printf("\\n");')
        self.write_newline(outfile)

    def _get_hex_format_string(self, size):
        if size == 8:
            return "0x%016\" PRIx8 \""
        elif size == 16:
            return "0x%016\" PRIx16 \""
        elif size == 32:
            return "0x%016\" PRIx32 \""
        else:
            return "0x%016\" PRIx64 \""
