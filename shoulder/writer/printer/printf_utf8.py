import shoulder.gadget
from shoulder.config import config
from shoulder.writer.printer.printer import PrinterWriter


class PrintfUtf8PrinterWriter(PrinterWriter):

    def declare_fieldset_printer(self, outfile, register, fieldset):
        self._declare_fieldset_printer_from_value(outfile, register, fieldset)
        self._declare_fieldset_printer(outfile, register, fieldset)

    def declare_field_printer(self, outfile, register, field):
        self._declare_field_printer_from_value(outfile, register, field)
        self._declare_field_printer(outfile, register, field)

    # -------------------------------------------------------------------------
    # private
    # -------------------------------------------------------------------------

    def _declare_fieldset_printer(self, outfile, register, fieldset):
        gadget = self.gadgets["shoulder.cxx.function_definition"]
        gadget.name = config.print_function
        gadget.return_type = "void"
        gadget.args = []

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))
            gadget.name = gadget.name + "_at_index"

        self._declare_fieldset_printer_details(outfile, register, fieldset)

    @shoulder.gadget.cxx.function_definition
    def _declare_fieldset_printer_details(self, outfile, register, fieldset):
        self.call_register_get(outfile, register, "register_value", index="index")
        outfile.write(config.print_function + "(register_value);")

    def _declare_fieldset_printer_from_value(self, outfile, register, fieldset):
        if register.size == 32:
            size_type = "uint32_t"
        else:
            size_type = "uint64_t"
        gadget = self.gadgets["shoulder.cxx.function_definition"]
        gadget.name = config.print_function
        gadget.return_type = "void"
        gadget.args = [(size_type, "value")]

        self._declare_fieldset_printer_from_value_details(outfile, register, fieldset)

    @shoulder.gadget.cxx.function_definition
    def _declare_fieldset_printer_from_value_details(self, outfile, register, fieldset):
        if register.size == 32:
            outfile.write('printf("0x%016x %s", ')
        else:
            outfile.write('printf("0x%016lx %s", ')
        outfile.write('value, name);')
        self.write_newline(outfile)

        if register.long_name:
            outfile.write('printf(" (%s)", long_name);')
            self.write_newline(outfile)

        outfile.write('printf("\\n");')
        self.write_newline(outfile)

        for field in fieldset.fields:
            outfile.write(field.name.lower() + "::" + config.print_function + "(value);")
            self.write_newline(outfile)

    def _declare_field_printer(self, outfile, register, field):
        gadget = self.gadgets["shoulder.cxx.function_definition"]
        gadget.name = config.print_function
        gadget.return_type = "void"
        gadget.args = []

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))
            gadget.name = gadget.name + "_at_index"

        self._declare_field_printer_details(outfile, register, field)

    @shoulder.gadget.cxx.function_definition
    def _declare_field_printer_details(self, outfile, register, field):
        self.call_register_get(outfile, register, "register_value", index="index")
        self.call_field_get(outfile, "register_value", field, "field_value")

        outfile.write(config.print_function + "(field_value);")

    def _declare_field_printer_from_value(self, outfile, register, field):
        if register.size == 32:
            size_type = "uint32_t"
        else:
            size_type = "uint64_t"
        gadget = self.gadgets["shoulder.cxx.function_definition"]
        gadget.name = config.print_function
        gadget.return_type = "void"
        gadget.args = [(size_type, "register_value")]

        self._declare_field_printer_value_details(outfile, register, field)

    @shoulder.gadget.cxx.function_definition
    def _declare_field_printer_value_details(self, outfile, register, field):
        self.call_field_get(outfile, "register_value", field, "field_value")

        if field.msb == field.lsb:
            outfile.write('printf("    [%02u:%02u] %-16s%s%-20s", ')
            outfile.write('lsb, msb, ')
            outfile.write('"", ')
            outfile.write('field_value ? ')
            outfile.write('"\\033[1;32m \\xE2\\x9C\\x93 \\033[0m" : ')
            outfile.write('"\\033[1;31m \\xE2\\x9C\\x97 \\033[0m", ')
            outfile.write('name')
            outfile.write(');')
        else:
            if register.size == 32:
                outfile.write('printf("    [%02u:%02u] 0x%016x %-20s", ')
            else:
                outfile.write('printf("    [%02u:%02u] 0x%016lx %-20s", ')
            outfile.write('lsb, msb, field_value, name);')

        self.write_newline(outfile)

        if field.long_name:
            outfile.write('printf("(%s)", long_name);')
            self.write_newline(outfile)

        outfile.write('printf("\\n");')
        self.write_newline(outfile)
