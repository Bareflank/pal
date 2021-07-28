import pal.gadget


class CFieldAccessorWriter():

    def declare_field_accessors(self, outfile, register, field):
        self._declare_field_constants(outfile, register, field)

        if field.msb == field.lsb:
            if register.is_readable():
                self._declare_bitfield_is_enabled(outfile, register, field)
                self._declare_bitfield_is_enabled_in_value(outfile, register, field)
                self._declare_bitfield_is_disabled(outfile, register, field)
                self._declare_bitfield_is_disabled_in_value(outfile, register, field)
            if register.is_writeable():
                self._declare_bitfield_enable(outfile, register, field)
                self._declare_bitfield_enable_in_value(outfile, register, field)
                self._declare_bitfield_disable(outfile, register, field)
                self._declare_bitfield_disable_in_value(outfile, register, field)
        else:
            if register.is_readable():
                self._declare_get_field(outfile, register, field)
                self._declare_get_field_from_value(outfile, register, field)
            if register.is_writeable():
                self._declare_set_field(outfile, register, field)
                self._declare_set_field_in_value(outfile, register, field)

    def call_field_get(self, outfile, register, field, destination,
                       register_value):
        if field.msb == field.lsb:
            call = "{size} {dest} = pal_{component}{reg_name}_{field_name}_is_enabled_in_value({reg_val});".format(
                size=self._register_size_type(register),
                dest=destination,
                component = register.component.lower() + "_" if register.component else "",
                reg_name=register.name.lower(),
                field_name=field.name.lower(),
                reg_val=str(register_value)
            )
        else:
            call = "{size} {dest} = pal_get_{component}{reg_name}_{field_name}_from_value({reg_val});".format(
                size=self._register_size_type(register),
                dest=destination,
                component = register.component.lower() + "_" if register.component else "",
                reg_name=register.name.lower(),
                field_name=field.name.lower(),
                reg_val=str(register_value)
            )

        outfile.write(call)
        self.write_newline(outfile)

    # -------------------------------------------------------------------------
    # private
    # -------------------------------------------------------------------------
    def _declare_field_constants(self, outfile, register, field):
        prefix = self._field_prefix(register, field)

        name = prefix + "name"
        val = '"' + field.name.lower() + '"'
        self._declare_preprocessor_constant(outfile, name, val)

        if field.long_name:
            name = prefix + "long_name"
            val = '"' + field.long_name + '"'
            self._declare_preprocessor_constant(outfile, name, val)

        name = prefix + "lsb"
        val = str(field.lsb)
        self._declare_preprocessor_constant(outfile, name, val)

        name = prefix + "msb"
        val = str(field.msb)
        self._declare_preprocessor_constant(outfile, name, val)

        name = prefix + "mask"
        val = self._field_mask_hex_string(register, field)
        self._declare_preprocessor_constant(outfile, name, val)

        self.write_newline(outfile)

    def _declare_bitfield_is_enabled(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.c.function_definition"]
        gadget.return_type = size_type
        gadget.args = []
        gadget.name = self._bitfield_is_enabled_function_name(register, field)

        if register.component:
            view_type = self._view_type(register)
            gadget.args.append((view_type, "view"))

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))

        self._declare_bitfield_is_enabled_details(outfile, register, field)

    @pal.gadget.c.function_definition
    def _declare_bitfield_is_enabled_details(self, outfile, register, field):
        self.call_register_get(outfile, register, "value")

        return_statement = "return (value & {mask}) != 0;".format(
            mask=self._field_mask_string(register, field),
        )
        outfile.write(return_statement)

    def _declare_bitfield_is_enabled_in_value(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.c.function_definition"]
        gadget.return_type = size_type
        gadget.name = self._bitfield_is_enabled_in_value_function_name(register, field)
        gadget.args = [(size_type, "value")]

        self._declare_bitfield_is_enabled_in_val_details(outfile, register, field)

    @pal.gadget.c.function_definition
    def _declare_bitfield_is_enabled_in_val_details(self, outfile, register, field):
        f_body = "return (value & {mask}) != 0;".format(
            mask=self._field_mask_string(register, field)
        )

        outfile.write(f_body)

    def _declare_bitfield_is_disabled(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.c.function_definition"]
        gadget.return_type = size_type
        gadget.args = []
        gadget.name = self._bitfield_is_disabled_function_name(register, field)

        if register.component:
            view_type = self._view_type(register)
            gadget.args.append((view_type, "view"))

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))

        self._declare_bitfield_is_disabled_details(outfile, register, field)

    @pal.gadget.c.function_definition
    def _declare_bitfield_is_disabled_details(self, outfile, register, field):
        self.call_register_get(outfile, register, "value")

        return_statement = "return (value & {mask}) == 0;".format(
            mask=self._field_mask_string(register, field),
        )
        outfile.write(return_statement)

    def _declare_bitfield_is_disabled_in_value(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.c.function_definition"]
        gadget.return_type = size_type
        gadget.name = self._bitfield_is_disabled_in_value_function_name(register, field)
        gadget.args = [(size_type, "value")]

        self._declare_bitfield_is_disabled_in_value_details(outfile, register, field)

    @pal.gadget.c.function_definition
    def _declare_bitfield_is_disabled_in_value_details(self, outfile, register, field):
        f_body = "return (value & {mask}) == 0;".format(
            mask=self._field_mask_string(register, field)
        )

        outfile.write(f_body)

    def _declare_bitfield_enable(self, outfile, register, field):
        gadget = self.gadgets["pal.c.function_definition"]
        gadget.return_type = "void"
        gadget.args = []
        gadget.name = self._bitfield_enable_function_name(register, field)

        if register.component:
            view_type = self._view_type(register)
            gadget.args.append((view_type, "view"))

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))

        self._declare_bitfield_enable_details(outfile, register, field)

    @pal.gadget.c.function_definition
    def _declare_bitfield_enable_details(self, outfile, register, field):
        self.call_register_get(outfile, register, "value")

        reg_set = "{reg_set}({view}{index}value | {mask});".format(
            reg_set=self._register_write_function_name(register),
            view="view, " if register.component else "",
            index="index, " if register.is_indexed else "",
            mask=self._field_mask_string(register, field),
        )
        outfile.write(reg_set)

    def _declare_bitfield_enable_in_value(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.c.function_definition"]
        gadget.return_type = size_type
        gadget.name = self._bitfield_enable_in_value_function_name(register, field)
        gadget.args = [(size_type, "value")]

        self._declare_bitfield_enable_in_value_details(outfile, register, field)

    @pal.gadget.c.function_definition
    def _declare_bitfield_enable_in_value_details(self, outfile, register, field):
        f_body = "return value | {mask};".format(
            mask=self._field_mask_string(register, field)
        )
        outfile.write(f_body)

    def _declare_bitfield_disable(self, outfile, register, field):
        gadget = self.gadgets["pal.c.function_definition"]
        gadget.return_type = "void"
        gadget.args = []
        gadget.name = self._bitfield_disable_function_name(register, field)

        if register.component:
            view_type = self._view_type(register)
            gadget.args.append((view_type, "view"))

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))

        self._declare_bitfield_disable_details(outfile, register, field)

    @pal.gadget.c.function_definition
    def _declare_bitfield_disable_details(self, outfile, register, field):
        self.call_register_get(outfile, register, "value")

        reg_set = "{reg_set}({view}{index}value & ~{mask});".format(
            reg_set=self._register_write_function_name(register),
            view="view, " if register.component else "",
            index="index, " if register.is_indexed else "",
            mask=self._field_mask_string(register, field),
        )

        outfile.write(reg_set)

    def _declare_bitfield_disable_in_value(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.c.function_definition"]
        gadget.return_type = size_type
        gadget.name = self._bitfield_disable_in_value_function_name(register, field)
        gadget.args = [(size_type, "value")]

        self._declare_bitfield_disable_in_value_details(outfile, register, field)

    @pal.gadget.c.function_definition
    def _declare_bitfield_disable_in_value_details(self, outfile, register, field):
        f_body = "return value & ~{mask};".format(
            mask=self._field_mask_string(register, field)
        )
        outfile.write(f_body)

    def _declare_get_field(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.c.function_definition"]
        gadget.return_type = size_type
        gadget.args = []
        gadget.name = self._field_read_function_name(register, field)

        if register.component:
            view_type = self._view_type(register)
            gadget.args.append((view_type, "view"))

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))

        self._declare_get_field_details(outfile, register, field)

    @pal.gadget.c.function_definition
    def _declare_get_field_details(self, outfile, register, field):
        self.call_register_get(outfile, register, "value")

        return_statement = "return (value & {mask}) >> {lsb};".format(
            mask=self._field_mask_string(register, field),
            lsb=self._field_lsb_string(register, field),
        )
        outfile.write(return_statement)

    def _declare_get_field_from_value(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.c.function_definition"]
        gadget.return_type = size_type
        gadget.name = self._field_read_from_value_function_name(register, field)
        gadget.args = [(size_type, "value")]

        self._declare_get_field_from_value_details(outfile, register, field)

    @pal.gadget.c.function_definition
    def _declare_get_field_from_value_details(self, outfile, register, field):
        f_body = "return (value & {mask}) >> {lsb};".format(
            size=self._register_size_type(register),
            mask=self._field_mask_string(register, field),
            lsb=self._field_lsb_string(register, field)
        )

        outfile.write(f_body)

    def _declare_set_field(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.c.function_definition"]
        gadget.return_type = "void"
        gadget.name = self._field_write_function_name(register, field)
        gadget.args = []

        if register.component:
            view_type = self._view_type(register)
            gadget.args.append((view_type, "view"))

        gadget.args.append((size_type, "value"))

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))

        self._declare_field_set_details(outfile, register, field)

    @pal.gadget.c.function_definition
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

    def _declare_set_field_in_value(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.c.function_definition"]
        gadget.return_type = size_type
        gadget.args = [(size_type, "field_value"), (size_type, "register_value")]
        gadget.name = self._field_write_in_value_function_name(register, field)

        self._declare_set_field_in_value_details(outfile, register, field)

    @pal.gadget.c.function_definition
    def _declare_set_field_in_value_details(self, outfile, register, field):
        old_field_removed = "register_value = register_value & ~{mask};".format(
            mask=self._field_mask_string(register, field),
        )

        new_field_added = "return register_value | ((field_value << {lsb}) & {mask});".format(
            mask=self._field_mask_string(register, field),
            lsb=self._field_lsb_string(register, field),
        )

        outfile.write(old_field_removed)
        self.write_newline(outfile)
        outfile.write(new_field_added)
