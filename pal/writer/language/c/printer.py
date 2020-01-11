import pal.gadget
from pal.config import config


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
        prefix = self._register_prefix(register)

        if len(register.fieldsets) > 1:
            prefix = prefix + fieldset.name.lower() + "_"

        gadget = self.gadgets["pal.c.function_definition"]
        gadget.name = prefix + config.print_function
        gadget.return_type = "void"
        gadget.args = []

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))
            gadget.name = gadget.name + "_at_index"

        self._declare_fieldset_print_details(outfile, register, fieldset)

    @pal.gadget.c.function_definition
    def _declare_fieldset_print_details(self, outfile, register, fieldset):
        prefix = self._register_prefix(register)
        if len(register.fieldsets) > 1:
            prefix = prefix + fieldset.name.lower() + "_"

        self.call_register_get(outfile, register, "register_value")

        outfile.write(prefix + config.print_function + "_from_value(register_value);")

    def _declare_fieldset_print_value(self, outfile, register, fieldset):
        prefix = self._register_prefix(register)

        if len(register.fieldsets) > 1:
            prefix = prefix + fieldset.name.lower() + "_"

        size_type = self._register_size_type(register)
        gadget = self.gadgets["pal.c.function_definition"]
        gadget.name = prefix + config.print_function + "_from_value"
        gadget.return_type = "void"
        gadget.args = [(size_type, "value")]

        self._declare_fieldset_print_value_details(outfile, register, fieldset)

    @pal.gadget.c.function_definition
    def _declare_fieldset_print_value_details(self, outfile, register, fieldset):
        self.print_value_as_register(outfile, register, "value")
        for field in fieldset.fields:
            prefix = self._field_prefix(register, field)
            outfile.write(prefix + config.print_function + "_from_value(value);")
            self.write_newline(outfile)

    def _declare_field_print(self, outfile, register, field):
        prefix = self._field_prefix(register, field)
        gadget = self.gadgets["pal.c.function_definition"]
        gadget.name = prefix + config.print_function
        gadget.return_type = "void"
        gadget.args = []

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))
            gadget.name = gadget.name + "_at_index"

        self._declare_field_print_details(outfile, register, field)

    @pal.gadget.c.function_definition
    def _declare_field_print_details(self, outfile, register, field):
        self.call_register_get(outfile, register, "register_value")
        self.call_field_get(outfile, register, field, "field_value",
                            "register_value")

        prefix = self._field_prefix(register, field)
        outfile.write(prefix + config.print_function + "_from_value(field_value);")

    def _declare_field_print_value(self, outfile, register, field):
        prefix = self._field_prefix(register, field)
        size_type = self._register_size_type(register)
        gadget = self.gadgets["pal.c.function_definition"]
        gadget.name = prefix + config.print_function + "_from_value"
        gadget.return_type = "void"
        gadget.args = [(size_type, "register_value")]

        self._declare_field_print_value_details(outfile, register, field)

    @pal.gadget.c.function_definition
    def _declare_field_print_value_details(self, outfile, register, field):
        self.call_field_get(outfile, register, field, "field_value", "register_value")

        self.print_value_as_field(outfile, register, field, "field_value")
