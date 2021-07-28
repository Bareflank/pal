import pal.gadget


class CPrinterWriter():

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
        gadget = self.gadgets["pal.c.function_definition"]
        gadget.name = self._fieldset_print_function_name(register, fieldset)
        gadget.return_type = "void"
        gadget.args = [("int" , "(*printf_ptr) (char const *str, ...)")]

        if register.component:
            view_type = self._view_type(register)
            gadget.args.append((view_type, "view"))

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))

        self._declare_fieldset_print_details(outfile, register, fieldset)

    @pal.gadget.c.function_definition
    def _declare_fieldset_print_details(self, outfile, register, fieldset):
        self.call_register_get(outfile, register, "register_value")
        print_fieldset_code = "{function_name}(printf_ptr, register_value);".format(
            function_name=self._fieldset_print_from_value_function_name(register, fieldset)
        )
        outfile.write(print_fieldset_code)

    def _declare_fieldset_print_value(self, outfile, register, fieldset):
        size_type = self._register_size_type(register)
        gadget = self.gadgets["pal.c.function_definition"]
        gadget.name = self._fieldset_print_from_value_function_name(register, fieldset)
        gadget.return_type = "void"
        gadget.args = [("int" , "(*printf_ptr) (char const *str, ...)"), (size_type, "value")]

        self._declare_fieldset_print_value_details(outfile, register, fieldset)

    @pal.gadget.c.function_definition
    def _declare_fieldset_print_value_details(self, outfile, register, fieldset):
        self.print_value_as_register(outfile, register, "value")
        for field in fieldset.fields:
            print_field_code = "{function_name}(printf_ptr, value);".format(
                function_name=self._field_print_from_value_function_name(register, field)
            )
            outfile.write(print_field_code)
            self.write_newline(outfile)

    def _declare_field_print(self, outfile, register, field):
        gadget = self.gadgets["pal.c.function_definition"]
        gadget.name = self._field_print_function_name(register, field)
        gadget.return_type = "void"
        gadget.args = [("int" , "(*printf_ptr) (char const *str, ...)")]

        if register.component:
            view_type = self._view_type(register)
            gadget.args.append((view_type, "view"))

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))

        self._declare_field_print_details(outfile, register, field)

    @pal.gadget.c.function_definition
    def _declare_field_print_details(self, outfile, register, field):
        self.call_register_get(outfile, register, "register_value")
        self.call_field_get(outfile, register, field, "field_value",
                            "register_value")

        print_field_code = "{function_name}(printf_ptr, field_value);".format(
            function_name=self._field_print_from_value_function_name(register, field)
        )
        outfile.write(print_field_code)

    def _declare_field_print_value(self, outfile, register, field):
        size_type = self._register_size_type(register)
        gadget = self.gadgets["pal.c.function_definition"]
        gadget.name = self._field_print_from_value_function_name(register, field)
        gadget.return_type = "void"
        gadget.args = [("int" , "(*printf_ptr) (char const *str, ...)"), (size_type, "register_value")]

        self._declare_field_print_value_details(outfile, register, field)

    @pal.gadget.c.function_definition
    def _declare_field_print_value_details(self, outfile, register, field):
        self.call_field_get(outfile, register, field, "field_value", "register_value")

        self.print_value_as_field(outfile, register, field, "field_value")
