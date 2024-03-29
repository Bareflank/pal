class CHelperWriter():

    def _field_mask_hex_string(self, register, field):
        mask_val = 0
        for i in range(field.lsb, field.msb + 1):
            mask_val |= 1 << i

        if register.size == 32:
            return "{0:#0{1}x}".format(mask_val, 10)
        else:
            return "{0:#0{1}x}".format(mask_val, 18)

    def _field_mask_string(self, register, field):
        return "pal_{component}{register}_{field}_mask".format(
            component = register.component.lower() + "_" if register.component else "",
            register=register.name.lower(),
            field=field.name.lower()
        ).upper()

    def _field_lsb_string(self, register, field):
        return "pal_{component}{register}_{field}_lsb".format(
            component = register.component.lower() + "_" if register.component else "",
            register=register.name.lower(),
            field=field.name.lower()
        ).upper()

    def _register_size_type(self, register):
        if register.size == 8:
            return "uint8_t"
        if register.size == 16:
            return "uint16_t"
        if register.size == 32:
            return "uint32_t"
        else:
            return "uint64_t"

    def _address_size_type(self, access_mechanism):
        if access_mechanism.name == "read_pci_config":
            return "uint16_t"
        if access_mechanism.name == "write_pci_config":
            return "uint16_t"
        else:
            return "uintptr_t"

    def _view_name(self, register):
        return "pal_" + register.component.lower() + "_view"

    def _view_type(self, register):
        return "const " + self._view_name(register) + " *"

    def _declare_variable(self, outfile, name, value, keywords=[]):
        for qual in keywords:
            outfile.write(str(qual) + " ")

        outfile.write(str(name) + " = " + str(value) + ";")
        self.write_newline(outfile)

    def _declare_hex_integer_constant(self, outfile, name, value):
        outfile.write("static const uintptr_t " + str(name) + " = " +
                      str(hex(value)) + ";")

    def _declare_preprocessor_constant(self, outfile, name, value):
        outfile.write("#define " + str(name).upper() + " " +
                      str(value))
        self.write_newline(outfile)

    def _declare_string_constant(self, outfile, name, value):
        outfile.write('static const char *' + str(name) + ' = "' +
                      str(value) + '";')

    def _register_read_function_name(self, register):
        return "pal_get_{component}{reg_name}{at_index}".format(
            component = register.component.lower() + "_" if register.component else "",
            reg_name=register.name.lower(),
            at_index="_at_index" if register.is_indexed else ""
        )

    def _register_write_function_name(self, register):
        return "pal_set_{component}{reg_name}{at_index}".format(
            component = register.component.lower() + "_" if register.component else "",
            reg_name=register.name.lower(),
            at_index="_at_index" if register.is_indexed else ""
        )

    def _bitfield_enable_function_name(self, register, field):
        return "pal_enable_{component}{reg_name}_{field_name}{at_index}".format(
            component = register.component.lower() + "_" if register.component else "",
            reg_name=register.name.lower(),
            field_name=field.name.lower(),
            at_index="_at_index" if register.is_indexed else ""
        )

    def _bitfield_enable_in_value_function_name(self, register, field):
        return "pal_enable_{component}{reg_name}_{field_name}_in_value".format(
            component = register.component.lower() + "_" if register.component else "",
            reg_name=register.name.lower(),
            field_name=field.name.lower()
        )

    def _bitfield_is_enabled_function_name(self, register, field):
        return "pal_{component}{reg_name}_{field_name}_is_enabled{at_index}".format(
            component = register.component.lower() + "_" if register.component else "",
            reg_name=register.name.lower(),
            field_name=field.name.lower(),
            at_index="_at_index" if register.is_indexed else ""
        )

    def _bitfield_is_enabled_in_value_function_name(self, register, field):
        return "pal_{component}{reg_name}_{field_name}_is_enabled_in_value".format(
            component = register.component.lower() + "_" if register.component else "",
            reg_name=register.name.lower(),
            field_name=field.name.lower()
        )

    def _bitfield_disable_function_name(self, register, field):
        return "pal_disable_{component}{reg_name}_{field_name}{at_index}".format(
            component = register.component.lower() + "_" if register.component else "",
            reg_name=register.name.lower(),
            field_name=field.name.lower(),
            at_index="_at_index" if register.is_indexed else ""
        )

    def _bitfield_disable_in_value_function_name(self, register, field):
        return "pal_disable_{component}{reg_name}_{field_name}_in_value".format(
            component = register.component.lower() + "_" if register.component else "",
            reg_name=register.name.lower(),
            field_name=field.name.lower()
        )

    def _bitfield_is_disabled_function_name(self, register, field):
        return "pal_{component}{reg_name}_{field_name}_is_disabled{at_index}".format(
            component = register.component.lower() + "_" if register.component else "",
            reg_name=register.name.lower(),
            field_name=field.name.lower(),
            at_index="_at_index" if register.is_indexed else ""
        )

    def _bitfield_is_disabled_in_value_function_name(self, register, field):
        return "pal_{component}{reg_name}_{field_name}_is_disabled_in_value".format(
            component = register.component.lower() + "_" if register.component else "",
            reg_name=register.name.lower(),
            field_name=field.name.lower()
        )

    def _field_read_function_name(self, register, field):
        return "pal_get_{component}{reg_name}_{field_name}{at_index}".format(
            component = register.component.lower() + "_" if register.component else "",
            reg_name=register.name.lower(),
            field_name=field.name.lower(),
            at_index="_at_index" if register.is_indexed else ""
        )

    def _field_read_from_value_function_name(self, register, field):
        return "pal_get_{component}{reg_name}_{field_name}_from_value".format(
            component = register.component.lower() + "_" if register.component else "",
            reg_name=register.name.lower(),
            field_name=field.name.lower()
        )

    def _field_write_function_name(self, register, field):
        return "pal_set_{component}{reg_name}_{field_name}{at_index}".format(
            component = register.component.lower() + "_" if register.component else "",
            reg_name=register.name.lower(),
            field_name=field.name.lower(),
            at_index="_at_index" if register.is_indexed else ""
        )

    def _field_write_in_value_function_name(self, register, field):
        return "pal_set_{component}{reg_name}_{field_name}_in_value".format(
            component = register.component.lower() + "_" if register.component else "",
            reg_name=register.name.lower(),
            field_name=field.name.lower()
        )

    def _field_print_function_name(self, register, field):
        return "pal_print_{component}{reg_name}_{field_name}{at_index}".format(
            component = register.component.lower() + "_" if register.component else "",
            reg_name=register.name.lower(),
            field_name=field.name.lower(),
            at_index="_at_index" if register.is_indexed else ""
        )

    def _field_print_from_value_function_name(self, register, field):
        return "pal_print_{component}{reg_name}_{field_name}_from_value".format(
            component = register.component.lower() + "_" if register.component else "",
            reg_name=register.name.lower(),
            field_name=field.name.lower()
        )

    def _fieldset_print_function_name(self, register, fieldset):
        return "pal_print_{component}{reg_name}{fieldset_name}{at_index}".format(
            component = register.component.lower() + "_" if register.component else "",
            reg_name=register.name.lower(),
            fieldset_name="_" + fieldset.name.lower() if len(register.fieldsets) > 1 else "",
            at_index="_at_index" if register.is_indexed else ""
        )

    def _fieldset_print_from_value_function_name(self, register, fieldset):
        return "pal_print_{component}{reg_name}{fieldset_name}_from_value".format(
            component = register.component.lower() + "_" if register.component else "",
            reg_name=register.name.lower(),
            fieldset_name="_" + fieldset.name.lower() if len(register.fieldsets) > 1 else ""
        )

    def _register_prefix(self, register):
        return "pal_{component}{reg_name}_".format(
            component = register.component.lower() + "_" if register.component else "",
            reg_name=register.name.lower()
        )

    def _field_prefix(self, register, field):
        return "pal_{component}{reg_name}_{field_name}_".format(
            component = register.component.lower() + "_" if register.component else "",
            reg_name=register.name.lower(),
            field_name=field.name.lower()
        )
