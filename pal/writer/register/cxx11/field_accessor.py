import pal.gadget


class Cxx11FieldAccessorWriter():

    def declare_field_accessors(self, outfile, register, field):
        self._declare_field_constants(outfile, register, field)

        if field.msb == field.lsb:
            if register.is_readable():
                self._declare_bitfield_is_set(outfile, register, field)
                self._declare_bitfield_is_set_val(outfile, register, field)
                self._declare_bitfield_is_clear(outfile, register, field)
                self._declare_bitfield_is_clear_val(outfile, register, field)
            if register.is_writeable():
                self._declare_bitfield_set(outfile, register, field)
                self._declare_bitfield_set_val(outfile, register, field)
                self._declare_bitfield_clear(outfile, register, field)
                self._declare_bitfield_clear_val(outfile, register, field)
        else:
            if register.is_readable():
                self._declare_field_get(outfile, register, field)
                self._declare_field_get_val(outfile, register, field)
            if register.is_writeable():
                self._declare_field_set(outfile, register, field)
                self._declare_field_set_val(outfile, register, field)

    def call_field_get(self, outfile, register, field, destination,
                       register_value):
        if field.msb == field.lsb:
            field_read_function = "is_enabled",
        else:
            field_read_function = "get",

        call = "auto {dest} = {field_name}::{read}({reg_val});".format(
            dest=destination,
            field_name=field.name.lower(),
            read=str(field_read_function[0]),
            reg_val=str(register_value)
        )
        outfile.write(call)
        self.write_newline(outfile)

    # -------------------------------------------------------------------------
    # private
    # -------------------------------------------------------------------------
    def _declare_field_constants(self, outfile, register, field):
        keywords = ["constexpr", "const", "auto"]
        name = "name"
        val = '"' + field.name.lower() + '"'
        self._declare_variable(outfile, name, value=val, keywords=keywords)

        if field.long_name:
            keywords = ["constexpr", "const", "auto"]
            name = "long_name"
            val = '"' + field.long_name + '"'
            self._declare_variable(outfile, name, value=val, keywords=keywords)

        keywords = ["constexpr", "const", "uint32_t"]
        name = "lsb"
        val = str(field.lsb)
        self._declare_variable(outfile, name, value=val, keywords=keywords)

        keywords = ["constexpr", "const", "uint32_t"]
        name = "msb"
        val = str(field.msb)
        self._declare_variable(outfile, name, value=val, keywords=keywords)

        keywords = ["constexpr", "const", self._register_size_type(register)]
        name = "mask"
        val = self._field_mask_hex_string(register, field)
        self._declare_variable(outfile, name, value=val, keywords=keywords)

        self.write_newline(outfile)

    def _declare_bitfield_is_set(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.cxx.function_definition"]
        gadget.return_type = size_type
        gadget.args = []
        gadget.name = "is_enabled"

        if register.component:
            view_type = self._view_type(register)
            gadget.args.append((view_type, "view"))

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))
            gadget.name = gadget.name + "_at_index"

        self._declare_bitfield_is_set_details(outfile, register, field)

    @pal.gadget.cxx.function_definition
    def _declare_bitfield_is_set_details(self, outfile, register, field):
        self.call_register_get(outfile, register, "value")

        return_statement = "return (value & {mask}) != 0;".format(
            mask=self._field_mask_string(register, field),
        )

        outfile.write(return_statement)

    def _declare_bitfield_is_set_val(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.cxx.function_definition"]
        gadget.return_type = size_type
        gadget.args = [(size_type, "value")]
        gadget.name = "is_enabled"

        self._declare_bitfield_is_set_val_details(outfile, register, field)

    @pal.gadget.cxx.function_definition
    def _declare_bitfield_is_set_val_details(self, outfile, register, field):
        f_body = "return (value & {mask}) != 0;".format(
            mask=self._field_mask_string(register, field)
        )

        outfile.write(f_body)

    def _declare_bitfield_is_clear(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.cxx.function_definition"]
        gadget.return_type = size_type
        gadget.args = []
        gadget.name = "is_disabled"

        if register.component:
            view_type = self._view_type(register)
            gadget.args.append((view_type, "view"))

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))
            gadget.name = gadget.name + "_at_index"

        self._declare_bitfield_is_clear_details(outfile, register, field)

    @pal.gadget.cxx.function_definition
    def _declare_bitfield_is_clear_details(self, outfile, register, field):
        self.call_register_get(outfile, register, "value")

        return_statement = "return (value & {mask}) == 0;".format(
            mask=self._field_mask_string(register, field),
        )

        outfile.write(return_statement)

    def _declare_bitfield_is_clear_val(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.cxx.function_definition"]
        gadget.return_type = size_type
        gadget.args = [(size_type, "value")]
        gadget.name = "is_disabled"

        self._declare_bitfield_is_clear_val_details(outfile, register, field)

    @pal.gadget.cxx.function_definition
    def _declare_bitfield_is_clear_val_details(self, outfile, register, field):
        f_body = "return (value & {mask}) == 0;".format(
            mask=self._field_mask_string(register, field)
        )

        outfile.write(f_body)

    def _declare_bitfield_set(self, outfile, register, field):
        gadget = self.gadgets["pal.cxx.function_definition"]
        gadget.return_type = "void"
        gadget.args = []
        gadget.name = "enable"

        if register.component:
            view_type = self._view_type(register)
            gadget.args.append((view_type, "view"))

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))
            gadget.name = gadget.name + "_at_index"

        self._declare_bitfield_set_details(outfile, register, field)

    @pal.gadget.cxx.function_definition
    def _declare_bitfield_set_details(self, outfile, register, field):
        self.call_register_get(outfile, register, "value")

        reg_set = "{reg_set}({view}{index}value | {mask});".format(
            mask=self._field_mask_string(register, field),
            view="view, " if register.component else "",
            reg_set=self._register_write_function_name(register),
            index="index, " if register.is_indexed else ""
        )

        outfile.write(reg_set)

    def _declare_bitfield_set_val(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.cxx.function_definition"]
        gadget.return_type = "void"
        gadget.args = [(size_type, "&value")]
        gadget.name = "enable"

        self._declare_bitfield_set_val_details(outfile, register, field)

    @pal.gadget.cxx.function_definition
    def _declare_bitfield_set_val_details(self, outfile, register, field):
        f_body = "value |= {mask};".format(
            mask=self._field_mask_string(register, field)
        )
        outfile.write(f_body)

    def _declare_bitfield_clear(self, outfile, register, field):
        gadget = self.gadgets["pal.cxx.function_definition"]
        gadget.return_type = "void"
        gadget.args = []
        gadget.name = "disable"

        if register.component:
            view_type = self._view_type(register)
            gadget.args.append((view_type, "view"))

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))
            gadget.name = gadget.name + "_at_index"

        self._declare_bitfield_clear_details(outfile, register, field)

    @pal.gadget.cxx.function_definition
    def _declare_bitfield_clear_details(self, outfile, register, field):
        self.call_register_get(outfile, register, "value")

        reg_set = "{reg_set}({view}{index}value & ~{mask});".format(
            mask=self._field_mask_string(register, field),
            view="view, " if register.component else "",
            reg_set=self._register_write_function_name(register),
            index="index, " if register.is_indexed else ""
        )

        outfile.write(reg_set)

    def _declare_bitfield_clear_val(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.cxx.function_definition"]
        gadget.return_type = "void"
        gadget.args = [(size_type, "&value")]
        gadget.name = "disable"

        self._declare_bitfield_clear_val_details(outfile, register, field)

    @pal.gadget.cxx.function_definition
    def _declare_bitfield_clear_val_details(self, outfile, register, field):
        f_body = "value &= ~{mask};".format(
            mask=self._field_mask_string(register, field)
        )
        outfile.write(f_body)

    def _declare_field_get(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.cxx.function_definition"]
        gadget.return_type = size_type
        gadget.args = []
        gadget.name = "get"

        if register.component:
            view_type = self._view_type(register)
            gadget.args.append((view_type, "view"))

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))
            gadget.name = gadget.name + "_at_index"

        self._declare_field_get_details(outfile, register, field)

    @pal.gadget.cxx.function_definition
    def _declare_field_get_details(self, outfile, register, field):
        self.call_register_get(outfile, register, "value")

        return_statement = "return (value & {mask}) >> {lsb};".format(
            mask=self._field_mask_string(register, field),
            lsb=self._field_lsb_string(register, field),
        )

        outfile.write(return_statement)

    def _declare_field_get_val(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.cxx.function_definition"]
        gadget.return_type = size_type
        gadget.args = [(size_type, "value")]
        gadget.name = "get"

        self._declare_field_get_val_details(outfile, register, field)

    @pal.gadget.cxx.function_definition
    def _declare_field_get_val_details(self, outfile, register, field):
        f_body = "return (value & {mask}) >> {lsb};".format(
            size=self._register_size_type(register),
            mask=self._field_mask_string(register, field),
            lsb=self._field_lsb_string(register, field)
        )

        outfile.write(f_body)

    def _declare_field_set(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.cxx.function_definition"]
        gadget.return_type = "void"
        gadget.args = []
        gadget.name = "set"

        if register.component:
            view_type = self._view_type(register)
            gadget.args.append((view_type, "view"))

        gadget.args.append((size_type, "value"))

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))
            gadget.name = gadget.name + "_at_index"

        self._declare_field_set_details(outfile, register, field)

    @pal.gadget.cxx.function_definition
    def _declare_field_set_details(self, outfile, register, field):
        self.call_register_get(outfile, register, "register_value")

        old_field_removed = "register_value = register_value & ~{mask};".format(
            mask=self._field_mask_string(register, field),
        )

        new_field_added = "register_value |= ((value << {lsb}) & {mask});".format(
            mask=self._field_mask_string(register, field),
            lsb=self._field_lsb_string(register, field),
        )

        reg_set = "{reg_set}({view}{index}register_value);".format(
            reg_set=self._register_write_function_name(register),
            view="view, " if register.component else "",
            index="index, " if register.is_indexed else "",
        )

        outfile.write(old_field_removed)
        self.write_newline(outfile)
        outfile.write(new_field_added)
        self.write_newline(outfile)
        outfile.write(reg_set)

    def _declare_field_set_val(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.cxx.function_definition"]
        gadget.return_type = "void"
        gadget.args = [(size_type, "field_value"), (size_type, "&register_value")]
        gadget.name = "set"

        self._declare_field_set_val_details(outfile, register, field)

    @pal.gadget.cxx.function_definition
    def _declare_field_set_val_details(self, outfile, register, field):
        old_field_removed = "register_value = register_value & ~{mask};".format(
            mask=self._field_mask_string(register, field),
        )

        new_field_added = "register_value |= ((field_value << {lsb}) & {mask});".format(
            mask=self._field_mask_string(register, field),
            lsb=self._field_lsb_string(register, field),
        )

        outfile.write(old_field_removed)
        self.write_newline(outfile)
        outfile.write(new_field_added)
