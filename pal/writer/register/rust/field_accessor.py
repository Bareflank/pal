import pal.gadget


class RustFieldAccessorWriter():

    def declare_field_accessors(self, outfile, register, field):
        self._declare_field_constants(outfile, register, field)

        if field.msb == field.lsb:
            if register.is_readable():
                self._declare_bitfield_is_enabled(outfile, register, field)
                self._declare_bitfield_is_disabled(outfile, register, field)

            self._declare_bitfield_is_enabled_in_value(outfile, register, field)
            self._declare_bitfield_is_disabled_in_value(outfile, register, field)

            if register.is_writeable():
                self._declare_bitfield_enable(outfile, register, field)
                self._declare_bitfield_disable(outfile, register, field)

            self._declare_bitfield_enable_in_value(outfile, register, field)
            self._declare_bitfield_disable_in_value(outfile, register, field)

        else:
            if register.is_readable():
                self._declare_get_field(outfile, register, field)

            self._declare_get_field_from_value(outfile, register, field)

            if register.is_writeable():
                self._declare_set_field(outfile, register, field)

            self._declare_set_field_in_value(outfile, register, field)

    def call_field_get(self, outfile, register, field, destination, register_value):
        if field.msb == field.lsb:
            call = "let {dest} = {field_name}_is_enabled_in_value({reg_val});".format(
                dest=destination,
                field_name=field.name.lower(),
                reg_val=str(register_value)
            )
        else:
            call = "let {dest} = get_{field_name}_from_value({reg_val});".format(
                dest=destination,
                field_name=field.name.lower(),
                reg_val=str(register_value)
            )

        outfile.write(call)
        self.write_newline(outfile)

    # -------------------------------------------------------------------------
    # private
    # -------------------------------------------------------------------------
    def _declare_field_constants(self, outfile, register, field):
        prefix = self._field_prefix(register, field).upper()
        register_size = self._register_size_type(register)

        name = prefix + "NAME"
        val = '"' + field.name.lower() + '"'
        self._declare_variable(outfile, name, val, size_type="&str", const=True)

        if field.long_name:
            name = prefix + "LONG_NAME"
            val = '"' + field.long_name + '"'
            self._declare_variable(outfile, name, val, size_type="&str", const=True)

        size_type = self._register_size_type(register)
        name = prefix + "LSB"
        val = str(field.lsb)
        self._declare_variable(outfile, name, value=val,
                               size_type=register_size, const=True)

        name = prefix + "MSB"
        val = str(field.msb)
        self._declare_variable(outfile, name, value=val,
                               size_type=register_size, const=True)

        name = prefix + "MASK"
        val = self._field_mask_hex_string(register, field)
        self._declare_variable(outfile, name, value=val,
                               size_type=register_size, const=True)

        self.write_newline(outfile)

    def _declare_bitfield_is_enabled(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.rust.function_definition"]
        gadget.return_type = "bool"
        gadget.args = []
        gadget.name = self._bitfield_is_enabled_function_name(register, field)
        gadget.documentation = self._field_documentation(register, field,
            'Returns whether "{friendly_name}" is currently enabled.'
        )

        if register.is_indexed:
            gadget.args.append(("usize", "index"))

        self._declare_bitfield_is_enabled_details(outfile, register, field)

    @pal.gadget.rust.function_definition
    def _declare_bitfield_is_enabled_details(self, outfile, register, field):
        reg_get = "{reg_get}({index})".format(
            reg_get=self._register_read_function_name(register),
            index="index" if register.is_indexed else "",
        )

        return_statement = "(value & {mask}) != 0".format(
            mask=self._field_mask_string(register, field),
        )

        size_type = self._register_size_type(register)
        self._declare_variable(outfile, "value", reg_get, size_type=size_type)
        outfile.write(return_statement)

    def _declare_bitfield_is_enabled_in_value(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.rust.function_definition"]
        gadget.return_type = "bool"
        gadget.args = [(size_type, "value")]
        gadget.name = self._bitfield_is_enabled_in_value_function_name(register, field)
        gadget.documentation = self._field_documentation(register, field,
            'Returns whether "{friendly_name}" is enabled in the given register value.'
        )

        self._declare_bitfield_is_enabled_in_val_details(outfile, register, field)

    @pal.gadget.rust.function_definition
    def _declare_bitfield_is_enabled_in_val_details(self, outfile, register, field):
        f_body = "(value & {mask}) != 0".format(
            mask=self._field_mask_string(register, field)
        )

        outfile.write(f_body)

    def _declare_bitfield_is_disabled(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.rust.function_definition"]
        gadget.return_type = "bool"
        gadget.args = []
        gadget.name = self._bitfield_is_disabled_function_name(register, field)
        gadget.documentation = self._field_documentation(register, field,
            'Returns whether "{friendly_name}" is currently disabled.'
        )

        if register.is_indexed:
            gadget.args.append(("usize", "index"))

        self._declare_bitfield_is_disabled_details(outfile, register, field)

    @pal.gadget.rust.function_definition
    def _declare_bitfield_is_disabled_details(self, outfile, register, field):
        reg_get = "{reg_get}({index})".format(
            reg_get=self._register_read_function_name(register),
            index="index" if register.is_indexed else "",
        )

        return_statement = "(value & {mask}) == 0".format(
            mask=self._field_mask_string(register, field),
        )

        size_type = self._register_size_type(register)
        self._declare_variable(outfile, "value", reg_get, size_type=size_type)
        outfile.write(return_statement)

    def _declare_bitfield_is_disabled_in_value(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.rust.function_definition"]
        gadget.return_type = "bool"
        gadget.args = [(size_type, "value")]
        gadget.name = self._bitfield_is_disabled_in_value_function_name(register, field)
        gadget.documentation = self._field_documentation(register, field,
            'Returns whether "{friendly_name}" is disabled in the given register value.'
        )

        self._declare_bitfield_is_disabled_in_value_details(outfile, register, field)

    @pal.gadget.rust.function_definition
    def _declare_bitfield_is_disabled_in_value_details(self, outfile, register, field):
        f_body = "(value & {mask}) == 0".format(
            mask=self._field_mask_string(register, field)
        )

        outfile.write(f_body)

    def _declare_bitfield_enable(self, outfile, register, field):
        gadget = self.gadgets["pal.rust.function_definition"]
        gadget.return_type = None
        gadget.args = []
        gadget.name = self._bitfield_enable_function_name(register, field)
        gadget.documentation = self._field_documentation(register, field,
            'Enables "{friendly_name}".'
        )

        if register.is_indexed:
            gadget.args.append(("usize", "index"))

        self._declare_bitfield_enable_details(outfile, register, field)

    @pal.gadget.rust.function_definition
    def _declare_bitfield_enable_details(self, outfile, register, field):
        reg_get = "{reg_get}({index})".format(
            reg_get=self._register_read_function_name(register),
            index="index" if register.is_indexed else "",
        )

        reg_set = "{reg_set}({index}value | {mask});".format(
            mask=self._field_mask_string(register, field),
            reg_set=self._register_write_function_name(register),
            index="index, " if register.is_indexed else ""
        )

        size_type = self._register_size_type(register)
        if register.is_readable():
            self._declare_variable(outfile, "value", reg_get, size_type=size_type)
        else:
            self._declare_variable(outfile, "value", "0", size_type=size_type)
        outfile.write(reg_set)

    def _declare_bitfield_enable_in_value(self, outfile, register, field):
        size_type = "&mut " + self._register_size_type(register)

        gadget = self.gadgets["pal.rust.function_definition"]
        gadget.return_type = None
        gadget.args = [(size_type, "value")]
        gadget.name = self._bitfield_enable_in_value_function_name(register, field)
        gadget.documentation = self._field_documentation(register, field,
            'Enables "{friendly_name}" in the given register value, returning the new value.'
        )

        self._declare_bitfield_enable_in_value_details(outfile, register, field)

    @pal.gadget.rust.function_definition
    def _declare_bitfield_enable_in_value_details(self, outfile, register, field):
        f_body = "*value |= {mask}".format(
            mask=self._field_mask_string(register, field)
        )
        outfile.write(f_body)

    def _declare_bitfield_disable(self, outfile, register, field):
        gadget = self.gadgets["pal.rust.function_definition"]
        gadget.return_type = None
        gadget.args = []
        gadget.name = self._bitfield_disable_function_name(register, field)
        gadget.documentation = self._field_documentation(register, field,
            'Disables "{friendly_name}".'
        )

        if register.is_indexed:
            gadget.args.append(("usize", "index"))

        self._declare_bitfield_disable_details(outfile, register, field)

    @pal.gadget.rust.function_definition
    def _declare_bitfield_disable_details(self, outfile, register, field):
        reg_get = "{reg_get}({index})".format(
            reg_get=self._register_read_function_name(register),
            index="index" if register.is_indexed else "",
        )

        reg_set = "{reg_set}({index}value & !{mask});".format(
            mask=self._field_mask_string(register, field),
            reg_set=self._register_write_function_name(register),
            index="index, " if register.is_indexed else ""
        )

        size_type = self._register_size_type(register)
        if register.is_readable():
            self._declare_variable(outfile, "value", reg_get, size_type=size_type)
        else:
            self._declare_variable(outfile, "value", "0", size_type=size_type)
        outfile.write(reg_set)

    def _declare_bitfield_disable_in_value(self, outfile, register, field):
        size_type = "&mut " + self._register_size_type(register)

        gadget = self.gadgets["pal.rust.function_definition"]
        gadget.return_type = None
        gadget.args = [(size_type, "value")]
        gadget.name = self._bitfield_disable_in_value_function_name(register, field)
        gadget.documentation = self._field_documentation(register, field,
            'Disables "{friendly_name}" in the given register value, returning the new value.'
        )

        self._declare_bitfield_disable_in_value_details(outfile, register, field)

    @pal.gadget.rust.function_definition
    def _declare_bitfield_disable_in_value_details(self, outfile, register, field):
        f_body = "*value &= !{mask};".format(
            mask=self._field_mask_string(register, field)
        )
        outfile.write(f_body)

    def _declare_get_field(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.rust.function_definition"]
        gadget.return_type = size_type
        gadget.args = []
        gadget.name = self._field_read_function_name(register, field)
        gadget.documentation = self._field_documentation(register, field,
            'Returns the current value of "{friendly_name}".'
        )

        if register.is_indexed:
            gadget.args.append(("usize", "index"))

        self._declare_get_field_details(outfile, register, field)

    @pal.gadget.rust.function_definition
    def _declare_get_field_details(self, outfile, register, field):
        reg_get = "{reg_get}({index})".format(
            reg_get=self._register_read_function_name(register),
            index="index" if register.is_indexed else "",
        )

        return_statement = "(value & {mask}) >> {lsb}".format(
            mask=self._field_mask_string(register, field),
            lsb=self._field_lsb_string(register, field),
        )

        size_type = self._register_size_type(register)
        self._declare_variable(outfile, "value", reg_get, size_type=size_type)
        outfile.write(return_statement)

    def _declare_get_field_from_value(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.rust.function_definition"]
        gadget.return_type = size_type
        gadget.args = [(size_type, "value")]
        gadget.name = self._field_read_from_value_function_name(register, field)
        gadget.documentation = self._field_documentation(register, field,
            'Returns the value of "{friendly_name}" in the given register value.'
        )

        self._declare_get_field_from_value_details(outfile, register, field)

    @pal.gadget.rust.function_definition
    def _declare_get_field_from_value_details(self, outfile, register, field):
        f_body = "(value & {mask}) >> {lsb}".format(
            size=self._register_size_type(register),
            mask=self._field_mask_string(register, field),
            lsb=self._field_lsb_string(register, field)
        )

        outfile.write(f_body)

    def _declare_set_field(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.rust.function_definition"]
        gadget.return_type = None
        gadget.args = [(size_type, "value")]
        gadget.name = self._field_write_function_name(register, field)
        gadget.documentation = self._field_documentation(register, field,
            'Sets the value of "{friendly_name}".'
        )

        if register.is_indexed:
            gadget.args.append(("usize", "index"))

        self._declare_field_set_details(outfile, register, field)

    @pal.gadget.rust.function_definition
    def _declare_field_set_details(self, outfile, register, field):
        reg_get = "{reg_get}({index})".format(
            reg_get=self._register_read_function_name(register),
            index="index" if register.is_indexed else "",
        )

        old_field_removed = "register_value = register_value & !{mask};".format(
            mask=self._field_mask_string(register, field),
        )

        new_field_added = "register_value |= (value << {lsb}) & {mask};".format(
            mask=self._field_mask_string(register, field),
            lsb=self._field_lsb_string(register, field),
        )

        reg_set = "{reg_set}(register_value);".format(
            reg_set=self._register_write_function_name(register),
        )

        size_type = self._register_size_type(register)

        if register.is_readable():
            self._declare_variable(outfile, "register_value", reg_get,
                                   size_type=size_type, mut=True)
            outfile.write(old_field_removed)
            self.write_newline(outfile)
        else:
            self._declare_variable(outfile, "register_value", "0",
                                   size_type=size_type, mut=True)

        outfile.write(new_field_added)
        self.write_newline(outfile)
        outfile.write(reg_set)

    def _declare_set_field_in_value(self, outfile, register, field):
        size_type = self._register_size_type(register)
        mutable_size_type = "&mut " + size_type

        gadget = self.gadgets["pal.rust.function_definition"]
        gadget.return_type = None
        gadget.args = [(size_type, "field_value"), (mutable_size_type, "register_value")]
        gadget.name = self._field_write_in_value_function_name(register, field)
        gadget.documentation = self._field_documentation(register, field,
            'Sets the value of "{friendly_name}" in the given register value, returning the new value.'
        )

        self._declare_set_field_in_value_details(outfile, register, field)

    @pal.gadget.rust.function_definition
    def _declare_set_field_in_value_details(self, outfile, register, field):
        old_field_removed = "*register_value &= !{mask};".format(
            mask=self._field_mask_string(register, field),
        )

        new_field_added = "*register_value |= (field_value << {lsb}) & {mask};".format(
            mask=self._field_mask_string(register, field),
            lsb=self._field_lsb_string(register, field),
        )

        outfile.write(old_field_removed)
        self.write_newline(outfile)
        outfile.write(new_field_added)
