import textwrap
import pal.gadget
from pal.config import config
from pal.writer.language.language import LanguageWriter


class Cxx11LanguageWriter(LanguageWriter):

    def declare_register_constants(self, outfile, register):
        self._declare_string_constant(outfile, "name", register.name.lower())
        self.write_newline(outfile)

        if register.long_name:
            self._declare_string_constant(outfile, "long_name", register.long_name)
            self.write_newline(outfile)

        if register.access_mechanisms.get("rdmsr"):
            addr = register.access_mechanisms["rdmsr"][0].address
            self._declare_hex_integer_constant(outfile, "address", addr)
            self.write_newline(outfile)

        self.write_newline(outfile)

    def declare_comment(self, outfile, comment, wrap=79):
        # Wrap at (wrap - 3) to account for " * "characters
        wrapped = textwrap.wrap(comment, width=(wrap - 3))
        outfile.write("/*")
        self.write_newline(outfile)
        for line in wrapped:
            outfile.write(" * " + str(line))
            self.write_newline(outfile)
        outfile.write("*/")
        self.write_newline(outfile)

    def declare_register_get(self, outfile, register):
        gadget = self.gadgets["pal.cxx.function_definition"]
        gadget.name = config.register_read_function
        gadget.return_type = self._register_size_type(register)
        gadget.args = []

        if register.is_indexed:
            gadget.args = [("uint32_t", "index")]
            gadget.name = gadget.name + "_at_index"

        self._declare_register_get_details(outfile, register)

    def declare_register_set(self, outfile, register):
        size_type = self._register_size_type(register)
        gadget = self.gadgets["pal.cxx.function_definition"]
        gadget.name = config.register_write_function
        gadget.return_type = "void"
        gadget.args = [(size_type, "value")]

        self._declare_register_set_details(outfile, register)

    def declare_field_constants(self, outfile, register, field):
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

    def declare_field_accessors(self, outfile, register, field):
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

    def call_register_get(self, outfile, register, destination, index="index"):
        call = "auto {dest} = {read}({index});".format(
            dest=destination,
            read=self._register_read_function_name(register),
            index=str(index) if register.is_indexed else ""
        )
        outfile.write(call)
        self.write_newline(outfile)

    def call_field_get(self, outfile, register_value, field, destination):
        if field.msb == field.lsb:
            field_read_function = str(config.bit_is_set_function),
        else:
            field_read_function = str(config.field_read_function),

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

    @pal.gadget.cxx.function_definition
    def _declare_register_get_details(self, outfile, register):
        for am_key, am_list in register.access_mechanisms.items():
            for access_mechanism in am_list:
                if access_mechanism.is_read():
                    size_type = self._register_size_type(register)
                    self._declare_variable(outfile, "value", 0, [size_type])
                    self.call_readable_access_mechanism(
                        outfile, register, access_mechanism, "value"
                    )
                    outfile.write("return value;")
                    return

    @pal.gadget.cxx.function_definition
    def _declare_register_set_details(self, outfile, register):
        for am_key, am_list in register.access_mechanisms.items():
            for access_mechanism in am_list:
                if access_mechanism.is_write():
                    self.call_writable_access_mechanism(
                        outfile, register, access_mechanism, "value"
                    )
                    return

    def _declare_bitfield_is_set(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.cxx.function_definition"]
        gadget.return_type = size_type
        gadget.args = []
        gadget.name = "{name}".format(
            name=config.bit_is_set_function
        )

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))
            gadget.name = gadget.name + "_at_index"

        self._declare_bitfield_is_set_details(outfile, register, field)

    @pal.gadget.cxx.function_definition
    def _declare_bitfield_is_set_details(self, outfile, register, field):
        reg_get = "{reg_get}({index})".format(
            reg_get=self._register_read_function_name(register),
            index="index" if register.is_indexed else "",
        )

        return_statement = "return (value & {mask}) != 0;".format(
            mask=self._field_mask_string(register, field),
        )

        self._declare_variable(outfile, "value", reg_get, ["auto"])
        outfile.write(return_statement)

    def _declare_bitfield_is_set_val(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.cxx.function_definition"]
        gadget.return_type = size_type
        gadget.args = [(size_type, "value")]
        gadget.name = "{name}".format(
            name=config.bit_is_set_function
        )

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
        gadget.name = "{name}".format(
            name=config.bit_is_clear_function
        )

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))
            gadget.name = gadget.name + "_at_index"

        self._declare_bitfield_is_clear_details(outfile, register, field)

    @pal.gadget.cxx.function_definition
    def _declare_bitfield_is_clear_details(self, outfile, register, field):
        reg_get = "{reg_get}({index})".format(
            reg_get=self._register_read_function_name(register),
            index="index" if register.is_indexed else "",
        )

        return_statement = "return (value & {mask}) == 0;".format(
            mask=self._field_mask_string(register, field),
        )

        self._declare_variable(outfile, "value", reg_get, ["auto"])
        outfile.write(return_statement)

    def _declare_bitfield_is_clear_val(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.cxx.function_definition"]
        gadget.return_type = size_type
        gadget.args = [(size_type, "value")]
        gadget.name = "{name}".format(
            name=config.bit_is_clear_function
        )

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
        gadget.name = "{name}".format(
            name=config.bit_set_function
        )

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))
            gadget.name = gadget.name + "_at_index"

        self._declare_bitfield_set_details(outfile, register, field)

    @pal.gadget.cxx.function_definition
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

        self._declare_variable(outfile, "value", reg_get, ["auto"])
        outfile.write(reg_set)

    def _declare_bitfield_set_val(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.cxx.function_definition"]
        gadget.return_type = "void"
        gadget.args = [(size_type, "&value")]
        gadget.name = "{name}".format(
            name=config.bit_set_function
        )

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
        gadget.name = "{name}".format(
            name=config.bit_clear_function
        )

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))
            gadget.name = gadget.name + "_at_index"

        self._declare_bitfield_clear_details(outfile, register, field)

    @pal.gadget.cxx.function_definition
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

        self._declare_variable(outfile, "value", reg_get, ["auto"])
        outfile.write(reg_set)

    def _declare_bitfield_clear_val(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.cxx.function_definition"]
        gadget.return_type = "void"
        gadget.args = [(size_type, "&value")]
        gadget.name = "{name}".format(
            name=config.bit_clear_function
        )

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
        gadget.name = "{name}".format(
            name=config.field_read_function
        )

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))
            gadget.name = gadget.name + "_at_index"

        self._declare_field_get_details(outfile, register, field)

    @pal.gadget.cxx.function_definition
    def _declare_field_get_details(self, outfile, register, field):
        reg_get = "{reg_get}({index})".format(
            reg_get=self._register_read_function_name(register),
            index="index" if register.is_indexed else "",
        )

        return_statement = "return (value & {mask}) >> {lsb};".format(
            mask=self._field_mask_string(register, field),
            lsb=self._field_lsb_string(register, field),
        )

        self._declare_variable(outfile, "value", reg_get, ["auto"])
        outfile.write(return_statement)

    def _declare_field_get_val(self, outfile, register, field):
        size_type = self._register_size_type(register)

        gadget = self.gadgets["pal.cxx.function_definition"]
        gadget.return_type = size_type
        gadget.args = [(size_type, "value")]
        gadget.name = "{name}".format(
            name=config.field_read_function
        )

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
        gadget.args = [(size_type, "value")]
        gadget.name = "{name}".format(
            name=config.field_write_function
        )

        if register.is_indexed:
            gadget.args.append(("uint32_t", "index"))
            gadget.name = gadget.name + "_at_index"

        self._declare_field_set_details(outfile, register, field)

    @pal.gadget.cxx.function_definition
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

        self._declare_variable(outfile, "register_value", reg_get, ["auto"])
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
        gadget.name = "{name}".format(
            name=config.field_write_function
        )

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
        outfile.write('printf("0x%016x %s (%s)\\n", ')
        outfile.write('value, name, long_name);')
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

        if field.msb == field.lsb:
            outfile.write('printf("    [%02u:%02u] %-16s%s%-20s", ')
            outfile.write('lsb, msb, ')
            outfile.write('"", ')
            outfile.write('field_value ? ')
            outfile.write('"\\033[1;32m \\xE2\\x9C\\x93 \\033[0m" : ')
            outfile.write('"\\033[1;31m \\xE2\\x9C\\x97 \\033[0m", ')
            outfile.write('name')
            outfile.write(');')
        else:
            outfile.write('printf("    [%02u:%02u] 0x%016x %-20s", ')
            outfile.write('lsb, msb, field_value, name);')

        if field.long_name:
            outfile.write('printf("(%s)", long_name);')

        outfile.write('printf("\\n");')

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
        if register.size == 32:
            return "uint32_t"
        else:
            return "uint64_t"

    def _register_read_function_name(self, register):
        return "{reg_name}::{read}{indexed}".format(
            reg_name=register.name.lower(),
            read=config.register_read_function,
            indexed="_at_index" if register.is_indexed else ""
        )

    def _register_write_function_name(self, register):
        return "{reg_name}::{write}".format(
            reg_name=register.name.lower(),
            write=config.register_write_function
        )

    def _bitfield_is_set_function_name(self, register, field):
        return "{field_name}::{read}{indexed}".format(
            field_name=field.name.lower(),
            read=config.bit_is_set_function,
            indexed="_at_index" if register.is_indexed else ""
        )

    def _field_read_function_name(self, register, field):
        return "{field_name}::{read}{indexed}".format(
            field_name=field.name.lower(),
            read=config.field_read_function,
            indexed="_at_index" if register.is_indexed else ""
        )

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
