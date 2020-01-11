import pal.gadget
from pal.config import config


class CFieldAccessorWriter():

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
            field_read_function = str(config.bit_is_set_function),
        else:
            field_read_function = str(config.field_read_function),

        call = "{size} {dest} = pal_{reg_name}_{field_name}_{read}_from_value({reg_val});".format(
            size=self._register_size_type(register),
            dest=destination,
            reg_name=register.name.lower(),
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
        prefix = self._field_prefix(register, field)

        keywords = ["const", "char", "*"]
        name = prefix + "name"
        val = '"' + field.name.lower() + '"'
        self._declare_variable(outfile, name, value=val, keywords=keywords)

        if field.long_name:
            keywords = ["const", "char", "*"]
            name = prefix + "long_name"
            val = '"' + field.long_name + '"'
            self._declare_variable(outfile, name, value=val, keywords=keywords)

        keywords = ["const", self._register_size_type(register)]
        name = prefix + "lsb"
        val = str(field.lsb)
        self._declare_variable(outfile, name, value=val, keywords=keywords)

        keywords = ["const", self._register_size_type(register)]
        name = prefix + "msb"
        val = str(field.msb)
        self._declare_variable(outfile, name, value=val, keywords=keywords)

        keywords = ["const", self._register_size_type(register)]
        name = prefix + "mask"
        val = self._field_mask_hex_string(register, field)
        self._declare_variable(outfile, name, value=val, keywords=keywords)

        self.write_newline(outfile)

    def _declare_bitfield_is_set(self, outfile, register, field):
        prefix = self._field_prefix(register, field)
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.c.function_definition"]
        gadget.return_type = size_type
        gadget.args = []
        gadget.name = prefix + "{name}".format(
            name=config.bit_is_set_function
        )

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))
            gadget.name = gadget.name + "_at_index"

        self._declare_bitfield_is_set_details(outfile, register, field)

    @pal.gadget.c.function_definition
    def _declare_bitfield_is_set_details(self, outfile, register, field):
        reg_get = "{reg_get}({index})".format(
            reg_get=self._register_read_function_name(register),
            index="index" if register.is_indexed else "",
        )

        return_statement = "return (value & {mask}) != 0;".format(
            mask=self._field_mask_string(register, field),
        )

        size_type = self._register_size_type(register)
        self._declare_variable(outfile, "value", reg_get, [size_type])
        outfile.write(return_statement)

    def _declare_bitfield_is_set_val(self, outfile, register, field):
        prefix = self._field_prefix(register, field)
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.c.function_definition"]
        gadget.return_type = size_type
        gadget.args = [(size_type, "value")]
        gadget.name = prefix + "{name}_from_value".format(
            name=config.bit_is_set_function
        )

        self._declare_bitfield_is_set_val_details(outfile, register, field)

    @pal.gadget.c.function_definition
    def _declare_bitfield_is_set_val_details(self, outfile, register, field):
        f_body = "return (value & {mask}) != 0;".format(
            mask=self._field_mask_string(register, field)
        )

        outfile.write(f_body)

    def _declare_bitfield_is_clear(self, outfile, register, field):
        prefix = self._field_prefix(register, field)
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.c.function_definition"]
        gadget.return_type = size_type
        gadget.args = []
        gadget.name = prefix + "{name}".format(
            name=config.bit_is_clear_function
        )

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))
            gadget.name = gadget.name + "_at_index"

        self._declare_bitfield_is_clear_details(outfile, register, field)

    @pal.gadget.c.function_definition
    def _declare_bitfield_is_clear_details(self, outfile, register, field):
        reg_get = "{reg_get}({index})".format(
            reg_get=self._register_read_function_name(register),
            index="index" if register.is_indexed else "",
        )

        return_statement = "return (value & {mask}) == 0;".format(
            mask=self._field_mask_string(register, field),
        )

        size_type = self._register_size_type(register)
        self._declare_variable(outfile, "value", reg_get, [size_type])
        outfile.write(return_statement)

    def _declare_bitfield_is_clear_val(self, outfile, register, field):
        prefix = self._field_prefix(register, field)
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.c.function_definition"]
        gadget.return_type = size_type
        gadget.args = [(size_type, "value")]
        gadget.name = prefix + "{name}_from_value".format(
            name=config.bit_is_clear_function
        )

        self._declare_bitfield_is_clear_val_details(outfile, register, field)

    @pal.gadget.c.function_definition
    def _declare_bitfield_is_clear_val_details(self, outfile, register, field):
        f_body = "return (value & {mask}) == 0;".format(
            mask=self._field_mask_string(register, field)
        )

        outfile.write(f_body)

    def _declare_bitfield_set(self, outfile, register, field):
        prefix = self._field_prefix(register, field)
        gadget = self.gadgets["pal.c.function_definition"]
        gadget.return_type = "void"
        gadget.args = []
        gadget.name = prefix + "{name}".format(
            name=config.bit_set_function
        )

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))
            gadget.name = gadget.name + "_at_index"

        self._declare_bitfield_set_details(outfile, register, field)

    @pal.gadget.c.function_definition
    def _declare_bitfield_set_details(self, outfile, register, field):
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
        self._declare_variable(outfile, "value", reg_get, [size_type])
        outfile.write(reg_set)

    def _declare_bitfield_set_val(self, outfile, register, field):
        prefix = self._field_prefix(register, field)
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.c.function_definition"]
        gadget.return_type = size_type
        gadget.args = [(size_type, "value")]
        gadget.name = prefix + "{name}_from_value".format(
            name=config.bit_set_function
        )

        self._declare_bitfield_set_val_details(outfile, register, field)

    @pal.gadget.c.function_definition
    def _declare_bitfield_set_val_details(self, outfile, register, field):
        f_body = "return value | {mask};".format(
            mask=self._field_mask_string(register, field)
        )
        outfile.write(f_body)

    def _declare_bitfield_clear(self, outfile, register, field):
        prefix = self._field_prefix(register, field)
        gadget = self.gadgets["pal.c.function_definition"]
        gadget.return_type = "void"
        gadget.args = []
        gadget.name = prefix + "{name}".format(
            name=config.bit_clear_function
        )

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))
            gadget.name = gadget.name + "_at_index"

        self._declare_bitfield_clear_details(outfile, register, field)

    @pal.gadget.c.function_definition
    def _declare_bitfield_clear_details(self, outfile, register, field):
        reg_get = "{reg_get}({index})".format(
            reg_get=self._register_read_function_name(register),
            index="index" if register.is_indexed else "",
        )

        reg_set = "{reg_set}({index}value & ~{mask});".format(
            mask=self._field_mask_string(register, field),
            reg_set=self._register_write_function_name(register),
            index="index, " if register.is_indexed else ""
        )

        size_type = self._register_size_type(register)
        self._declare_variable(outfile, "value", reg_get, [size_type])
        outfile.write(reg_set)

    def _declare_bitfield_clear_val(self, outfile, register, field):
        prefix = self._field_prefix(register, field)
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.c.function_definition"]
        gadget.return_type = size_type
        gadget.args = [(size_type, "value")]
        gadget.name = prefix + "{name}_from_value".format(
            name=config.bit_clear_function
        )

        self._declare_bitfield_clear_val_details(outfile, register, field)

    @pal.gadget.c.function_definition
    def _declare_bitfield_clear_val_details(self, outfile, register, field):
        f_body = "return value & ~{mask};".format(
            mask=self._field_mask_string(register, field)
        )
        outfile.write(f_body)

    def _declare_field_get(self, outfile, register, field):
        prefix = self._field_prefix(register, field)
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.c.function_definition"]
        gadget.return_type = size_type
        gadget.args = []
        gadget.name = prefix + "{name}".format(
            name=config.field_read_function
        )

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))
            gadget.name = gadget.name + "_at_index"

        self._declare_field_get_details(outfile, register, field)

    @pal.gadget.c.function_definition
    def _declare_field_get_details(self, outfile, register, field):
        reg_get = "{reg_get}({index})".format(
            reg_get=self._register_read_function_name(register),
            index="index" if register.is_indexed else "",
        )

        return_statement = "return (value & {mask}) >> {lsb};".format(
            mask=self._field_mask_string(register, field),
            lsb=self._field_lsb_string(register, field),
        )

        size_type = self._register_size_type(register)
        self._declare_variable(outfile, "value", reg_get, [size_type])
        outfile.write(return_statement)

    def _declare_field_get_val(self, outfile, register, field):
        prefix = self._field_prefix(register, field)
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.c.function_definition"]
        gadget.return_type = size_type
        gadget.args = [(size_type, "value")]
        gadget.name = prefix + "{name}_from_value".format(
            name=config.field_read_function
        )

        self._declare_field_get_val_details(outfile, register, field)

    @pal.gadget.c.function_definition
    def _declare_field_get_val_details(self, outfile, register, field):
        f_body = "return (value & {mask}) >> {lsb};".format(
            size=self._register_size_type(register),
            mask=self._field_mask_string(register, field),
            lsb=self._field_lsb_string(register, field)
        )

        outfile.write(f_body)

    def _declare_field_set(self, outfile, register, field):
        prefix = self._field_prefix(register, field)
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.c.function_definition"]
        gadget.return_type = "void"
        gadget.args = [(size_type, "value")]
        gadget.name = prefix + "{name}".format(
            name=config.field_write_function
        )

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))
            gadget.name = gadget.name + "_at_index"

        self._declare_field_set_details(outfile, register, field)

    @pal.gadget.c.function_definition
    def _declare_field_set_details(self, outfile, register, field):
        reg_get = "{reg_get}({index})".format(
            reg_get=self._register_read_function_name(register),
            index="index" if register.is_indexed else "",
        )

        old_field_removed = "register_value = register_value & ~{mask};".format(
            mask=self._field_mask_string(register, field),
        )

        new_field_added = "register_value |= ((value << {lsb}) & {mask});".format(
            mask=self._field_mask_string(register, field),
            lsb=self._field_lsb_string(register, field),
        )

        reg_set = "{reg_set}(register_value);".format(
            reg_set=self._register_write_function_name(register),
        )

        size_type = self._register_size_type(register)
        self._declare_variable(outfile, "register_value", reg_get, [size_type])
        outfile.write(old_field_removed)
        self.write_newline(outfile)
        outfile.write(new_field_added)
        self.write_newline(outfile)
        outfile.write(reg_set)

    def _declare_field_set_val(self, outfile, register, field):
        prefix = self._field_prefix(register, field)
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.c.function_definition"]
        gadget.return_type = size_type
        gadget.args = [(size_type, "field_value"), (size_type, "register_value")]
        gadget.name = prefix + "{name}_from_value".format(
            name=config.field_write_function
        )

        self._declare_field_set_val_details(outfile, register, field)

    @pal.gadget.c.function_definition
    def _declare_field_set_val_details(self, outfile, register, field):
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
