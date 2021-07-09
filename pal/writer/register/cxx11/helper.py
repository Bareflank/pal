class Cxx11HelperWriter():

    def _field_mask_hex_string(self, register, field):
        mask_val = 0
        for i in range(field.lsb, field.msb + 1):
            mask_val |= 1 << i

        if register.size == 32:
            return "{0:#0{1}x}".format(mask_val, 10)
        else:
            return "{0:#0{1}x}".format(mask_val, 18)

    def _field_mask_string(self, register, field):
        return "{field}::mask".format(
            field=field.name.lower()
        )

    def _field_lsb_string(self, register, field):
        return "{field}::lsb".format(
            field=field.name.lower()
        )

    def _register_size_type(self, register):
        if register.size == 8:
            return "uint8_t"
        if register.size == 16:
            return "uint16_t"
        if register.size == 32:
            return "uint32_t"
        else:
            return "uint64_t"

    def _declare_variable(self, outfile, name, value, keywords=[]):
        for qual in keywords:
            outfile.write(str(qual) + " ")

        outfile.write(str(name) + " = " + str(value) + ";")
        self.write_newline(outfile)

    def _declare_hex_integer_constant(self, outfile, name, value):
        outfile.write("constexpr const auto " + str(name) + " = " +
                      str(hex(value)) + ";")

    def _declare_string_constant(self, outfile, name, value):
        outfile.write('constexpr const auto ' + str(name) + ' = "' +
                      str(value) + '";')

    def _register_read_function_name(self, register):
        return "{reg_name}::get{indexed}".format(
            reg_name=register.name.lower(),
            indexed="_at_index" if register.is_indexed else ""
        )

    def _register_write_function_name(self, register):
        return "{reg_name}::set{indexed}".format(
            reg_name=register.name.lower(),
            indexed="_at_index" if register.is_indexed else ""
        )

    def _bitfield_is_set_function_name(self, register, field):
        return "{field_name}::is_enabled{indexed}".format(
            field_name=field.name.lower(),
            indexed="_at_index" if register.is_indexed else ""
        )

    def _field_read_function_name(self, register, field):
        return "{field_name}::get{indexed}".format(
            field_name=field.name.lower(),
            indexed="_at_index" if register.is_indexed else ""
        )
