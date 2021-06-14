from pal.writer.print_mechanism.print_mechanism import PrintMechanismWriter


class RustPrintlnPrintMechanismWriter(PrintMechanismWriter):

    def declare_print_mechanism_dependencies(self, outfile, register):
        for fs in register.fieldsets:
            for field in fs.fields:
                if field.msb == field.lsb:
                    outfile.write("use term;")
                    self.write_newline(outfile);
                    return

    def print_value_as_register(self, outfile, register, value):
        outfile.write('print!("0x{:016} ", ')
        outfile.write(str(value) + ');')
        self.write_newline(outfile)

        outfile.write('print!("' + str(register.name) + '");')
        self.write_newline(outfile)

        if register.long_name and register.long_name != register.name:
            outfile.write('print!(" (' + str(register.long_name) + ')");')
            self.write_newline(outfile)

        outfile.write('println!("");')
        self.write_newline(outfile)

    def print_value_as_field(self, outfile, register, field, value):
        outfile.write('print!("    ");')
        self.write_newline(outfile)

        outfile.write('print!("[{:02}:{:02}] ", ')
        outfile.write(str(field.msb) + ', ')
        outfile.write(str(field.lsb) + ');')
        self.write_newline(outfile)

        if field.msb == field.lsb:
            outfile.write('let mut terminal = term::stdout().unwrap();')
            self.write_newline(outfile)
            outfile.write('print!("{:-17}", "");')
            self.write_newline(outfile)
            outfile.write('match ' + str(value) + " {")
            self.write_newline(outfile)
            self.write_indent(outfile)
            outfile.write("false => {")
            self.write_newline(outfile)
            self.write_indent(outfile, count=2)
            outfile.write('terminal.fg(term::color::BRIGHT_RED).unwrap();')
            self.write_newline(outfile)
            self.write_indent(outfile, count=2)
            outfile.write('print!("{}", String::from_utf8(vec!(0xE2, 0x9C, 0x97)).unwrap());')
            self.write_newline(outfile)
            self.write_indent(outfile)
            outfile.write('},')
            self.write_newline(outfile)
            self.write_indent(outfile)
            outfile.write('true => {')
            self.write_newline(outfile)
            self.write_indent(outfile, count=2)
            outfile.write('terminal.fg(term::color::BRIGHT_GREEN).unwrap();')
            self.write_newline(outfile)
            self.write_indent(outfile, count=2)
            outfile.write('print!("{}", String::from_utf8(vec!(0xE2, 0x9C, 0x93)).unwrap());')
            self.write_newline(outfile)
            self.write_indent(outfile)
            outfile.write('},')
            self.write_newline(outfile)
            outfile.write('};')
            self.write_newline(outfile)
            outfile.write('terminal.reset().unwrap();')
            self.write_newline(outfile)
            outfile.write('print!("{:-2}", "");')
            self.write_newline(outfile)

        else:
            outfile.write('print!("0x{:016} ", ' + str(value) + ');')
            self.write_newline(outfile)

        outfile.write('print!("' + str(field.name) + '");')
        self.write_newline(outfile)

        if field.long_name and field.long_name != field.name:
            outfile.write('print!(" (' + str(field.long_name) + ')");')
            self.write_newline(outfile)

        outfile.write('println!("");')
        self.write_newline(outfile)
