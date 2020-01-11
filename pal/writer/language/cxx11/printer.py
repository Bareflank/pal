import pal.gadget
from pal.config import config


class Cxx11PrinterWriter():

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
        gadget = self.gadgets["pal.cxx.function_definition"]
        gadget.name = config.print_function
        gadget.return_type = "void"
        gadget.args = []

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))
            gadget.name = gadget.name + "_at_index"

        self._declare_fieldset_print_details(outfile, register, fieldset)

    @pal.gadget.cxx.function_definition
    def _declare_fieldset_print_details(self, outfile, register, fieldset):
        reg_get = "{reg_get}({index})".format(
            reg_get=self._register_read_function_name(register),
            index="index" if register.is_indexed else "",
        )
        keywords = ["auto"]
        name = "register_value"
        self._declare_variable(outfile, name, value=reg_get, keywords=keywords)

        outfile.write(config.print_function + "(register_value);")

    def _declare_fieldset_print_value(self, outfile, register, fieldset):
        size_type = self._register_size_type(register)
        gadget = self.gadgets["pal.cxx.function_definition"]
        gadget.name = config.print_function
        gadget.return_type = "void"
        gadget.args = [(size_type, "value")]

        self._declare_fieldset_print_value_details(outfile, register, fieldset)

    @pal.gadget.cxx.function_definition
    def _declare_fieldset_print_value_details(self, outfile, register, fieldset):
        self.print_value_as_register(outfile, register, "value")
        for field in fieldset.fields:
            outfile.write(field.name.lower() + "::" + config.print_function + "(value);")
            self.write_newline(outfile)

    def _declare_field_print(self, outfile, register, field):
        gadget = self.gadgets["pal.cxx.function_definition"]
        gadget.name = config.print_function
        gadget.return_type = "void"
        gadget.args = []

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))
            gadget.name = gadget.name + "_at_index"

        self._declare_field_print_details(outfile, register, field)

    @pal.gadget.cxx.function_definition
    def _declare_field_print_details(self, outfile, register, field):
        reg_get = "{reg_get}({index})".format(
            reg_get=self._register_read_function_name(register),
            index="index" if register.is_indexed else "",
        )
        keywords = ["auto"]
        name = "register_value"
        self._declare_variable(outfile, name, value=reg_get, keywords=keywords)

        if field.msb == field.lsb:
            field_get = "{field_get}(register_value)".format(
                field_get=self._bitfield_is_set_function_name(register, field),
            )
        else:
            field_get = "{field_get}(register_value)".format(
                field_get=self._field_read_function_name(register, field),
            )
        name = "field_value"
        self._declare_variable(outfile, name, value=field_get,
                               keywords=keywords)
        outfile.write(config.print_function + "(field_value);")

    def _declare_field_print_value(self, outfile, register, field):
        size_type = self._register_size_type(register)
        gadget = self.gadgets["pal.cxx.function_definition"]
        gadget.name = config.print_function
        gadget.return_type = "void"
        gadget.args = [(size_type, "register_value")]

        self._declare_field_print_value_details(outfile, register, field)

    @pal.gadget.cxx.function_definition
    def _declare_field_print_value_details(self, outfile, register, field):
        if field.msb == field.lsb:
            field_get = "{field_get}(register_value)".format(
                field_get=self._bitfield_is_set_function_name(register, field),
            )
        else:
            field_get = "{field_get}(register_value)".format(
                field_get=self._field_read_function_name(register, field),
            )
        keywords = ["auto"]
        name = "field_value"
        self._declare_variable(outfile, name, value=field_get,
                               keywords=keywords)

        self.print_value_as_field(outfile, register, field, name)
