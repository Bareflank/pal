class RustHelperWriter():

    def _field_mask_hex_string(self, register, field):
        mask_val = 0
        for i in range(field.lsb, field.msb + 1):
            mask_val |= 1 << i

        if register.size == 32:
            return "{0:#0{1}x}".format(mask_val, 10)
        else:
            return "{0:#0{1}x}".format(mask_val, 18)

    def _field_mask_string(self, register, field):
        return "{field}_MASK".format(
            field=field.name.upper()
        )

    def _field_lsb_string(self, register, field):
        return "{field}_LSB".format(
            field=field.name.upper()
        )

    def _register_size_type(self, register):
        return self._get_size_type(register.size)

    def _get_size_type(self, number_of_bits):
        if number_of_bits == 8:
            return "u8"
        if number_of_bits == 16:
            return "u16"
        if number_of_bits == 32:
            return "u32"
        if number_of_bits == 64:
            return "u64"
        else:
            return "usize"

    def _declare_variable(self, outfile, name, value, size_type=None, const=False, mut=False):
        if const:
            outfile.write("#[allow(dead_code)]")
            self.write_newline(outfile)
            outfile.write("const " + str(name))
        else:
            outfile.write("let ")
            if mut:
                outfile.write("mut ")
            outfile.write(str(name))

        if size_type:
            outfile.write(": " + str(size_type))

        outfile.write(" = " + str(value) + ";")
        self.write_newline(outfile)

    def _declare_hex_integer_constant(self, outfile, name, value, n_bits=None):
        outfile.write("#[allow(dead_code)]")
        self.write_newline(outfile)
        declaration = "pub const {name}: {size} = {value};".format(
            name=str(name).upper(),
            size=self._get_size_type(n_bits),
            value=str(hex(value))
        )
        outfile.write(declaration)

    def _declare_string_constant(self, outfile, name, value):
        outfile.write("#[allow(dead_code)]")
        self.write_newline(outfile)
        outfile.write('pub const ' + str(name).upper() + ': &str  = "' +
                      str(value) + '";')

    def _register_read_function_name(self, register):
        return "get{at_index}".format(
            at_index="_at_index" if register.is_indexed else ""
        )

    def _register_write_function_name(self, register):
        return "set{at_index}".format(
            at_index="_at_index" if register.is_indexed else ""
        )

    def _bitfield_enable_function_name(self, register, field):
        return "enable_{field_name}{at_index}".format(
            field_name=field.name.lower(),
            at_index="_at_index" if register.is_indexed else ""
        )

    def _bitfield_enable_in_value_function_name(self, register, field):
        return "enable_{field_name}_in_value".format(
            field_name=field.name.lower()
        )

    def _bitfield_is_enabled_function_name(self, register, field):
        return "{field_name}_is_enabled{at_index}".format(
            field_name=field.name.lower(),
            at_index="_at_index" if register.is_indexed else ""
        )

    def _bitfield_is_enabled_in_value_function_name(self, register, field):
        return "{field_name}_is_enabled_in_value".format(
            field_name=field.name.lower()
        )

    def _bitfield_disable_function_name(self, register, field):
        return "disable_{field_name}{at_index}".format(
            field_name=field.name.lower(),
            at_index="_at_index" if register.is_indexed else ""
        )

    def _bitfield_disable_in_value_function_name(self, register, field):
        return "disable_{field_name}_in_value".format(
            field_name=field.name.lower()
        )

    def _bitfield_is_disabled_function_name(self, register, field):
        return "{field_name}_is_disabled{at_index}".format(
            field_name=field.name.lower(),
            at_index="_at_index" if register.is_indexed else ""
        )

    def _bitfield_is_disabled_in_value_function_name(self, register, field):
        return "{field_name}_is_disabled_in_value".format(
            field_name=field.name.lower()
        )

    def _field_read_function_name(self, register, field):
        return "get_{field_name}{at_index}".format(
            field_name=field.name.lower(),
            at_index="_at_index" if register.is_indexed else ""
        )

    def _field_read_from_value_function_name(self, register, field):
        return "get_{field_name}_from_value".format(
            field_name=field.name.lower()
        )

    def _field_write_function_name(self, register, field):
        return "set_{field_name}{at_index}".format(
            field_name=field.name.lower(),
            at_index="_at_index" if register.is_indexed else ""
        )

    def _field_write_in_value_function_name(self, register, field):
        return "set_{field_name}_in_value".format(
            field_name=field.name.lower()
        )

    def _field_print_function_name(self, register, field):
        return "print_{field_name}{at_index}".format(
            field_name=field.name.lower(),
            at_index="_at_index" if register.is_indexed else ""
        )

    def _field_print_from_value_function_name(self, register, field):
        return "print_{field_name}_from_value".format(
            field_name=field.name.lower()
        )

    def _fieldset_print_function_name(self, register, fieldset):
        return "print{fieldset_name}{at_index}".format(
            fieldset_name="_" + fieldset.name.lower() if len(register.fieldsets) > 1 else "",
            at_index="_at_index" if register.is_indexed else ""
        )

    def _fieldset_print_from_value_function_name(self, register, fieldset):
        return "print{fieldset_name}_from_value".format(
            fieldset_name="_" + fieldset.name.lower() if len(register.fieldsets) > 1 else ""
        )

    def _register_prefix(self, register):
        return ""

    def _field_prefix(self, register, field):
        return "{field_name}_".format(
            field_name=field.name.lower()
        )
