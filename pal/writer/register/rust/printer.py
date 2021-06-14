import pal.gadget


class RustPrinterWriter():

    def declare_field_printers(self, outfile, register, field):
        self._declare_field_print_value(outfile, register, field)
        self._declare_field_print(outfile, register, field)

    def declare_fieldset_printers(self, outfile, register, fieldset):
        self._declare_fieldset_print_value(outfile, register, fieldset)
        self._declare_fieldset_print(outfile, register, fieldset)

    # -------------------------------------------------------------------------
    # private
    # -------------------------------------------------------------------------

    def _declare_fieldset_print(self, outfile, register, fieldset):
        gadget = self.gadgets["pal.rust.function_definition"]
        gadget.name = self._fieldset_print_function_name(register, fieldset)
        gadget.return_type = None
        gadget.args = []

        if register.is_indexed:
            gadget.args.append(("usize", "index"))

        self._declare_fieldset_print_details(outfile, register, fieldset)

    @pal.gadget.rust.function_definition
    def _declare_fieldset_print_details(self, outfile, register, fieldset):
        self.call_register_get(outfile, register, "register_value")
        print_fieldset_code = "{function_name}(register_value);".format(
            function_name=self._fieldset_print_from_value_function_name(register, fieldset)
        )
        outfile.write(print_fieldset_code)

    def _declare_fieldset_print_value(self, outfile, register, fieldset):
        size_type = self._register_size_type(register)
        gadget = self.gadgets["pal.rust.function_definition"]
        gadget.name = self._fieldset_print_from_value_function_name(register, fieldset)
        gadget.return_type = None
        gadget.args = [(size_type, "_value")]

        self._declare_fieldset_print_value_details(outfile, register, fieldset)

    @pal.gadget.rust.function_definition
    def _declare_fieldset_print_value_details(self, outfile, register, fieldset):
        self.print_value_as_register(outfile, register, "_value")
        for field in fieldset.fields:
            print_field_code = "{function_name}(_value);".format(
                function_name=self._field_print_from_value_function_name(register, field)
            )
            outfile.write(print_field_code)
            self.write_newline(outfile)

    def _declare_field_print(self, outfile, register, field):
        gadget = self.gadgets["pal.rust.function_definition"]
        gadget.name = self._field_print_function_name(register, field)
        gadget.return_type = None
        gadget.args = []

        if register.is_indexed:
            gadget.args.append(("usize", "index"))

        self._declare_field_print_details(outfile, register, field)

    @pal.gadget.rust.function_definition
    def _declare_field_print_details(self, outfile, register, field):
        self.call_register_get(outfile, register, "register_value")

        print_field_code = "{function_name}(register_value);".format(
            function_name=self._field_print_from_value_function_name(register, field)
        )
        outfile.write(print_field_code)

    def _declare_field_print_value(self, outfile, register, field):
        size_type = self._register_size_type(register)
        gadget = self.gadgets["pal.rust.function_definition"]
        gadget.name = self._field_print_from_value_function_name(register, field)
        gadget.return_type = None
        gadget.args = [(size_type, "register_value")]

        self._declare_field_print_value_details(outfile, register, field)

    @pal.gadget.rust.function_definition
    def _declare_field_print_value_details(self, outfile, register, field):
        self.call_field_get(outfile, register, field, "field_value", "register_value")

        self.print_value_as_field(outfile, register, field, "field_value")
