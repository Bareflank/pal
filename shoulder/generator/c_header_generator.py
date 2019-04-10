#
# Shoulder
# Copyright (C) 2018 Assured Information Security, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os

from shoulder.generator.abstract_generator import AbstractGenerator
from shoulder.register import Register
from shoulder.logger import logger
from shoulder.config import config
from shoulder.exception import *
from shoulder.gadget import *

class CHeaderGenerator(AbstractGenerator):
    def generate(self, objects, outpath):
        try:
            outfile_path = os.path.abspath(os.path.join(outpath, "shoulder.h"))
            logger.info("Generating C Header: " + str(outfile_path))
            with open(outfile_path, "w") as outfile:
                self._generate(outfile, objects)

        except Exception as e:
            msg = "{g} failed to generate output {out}: {exception}".format(
                g = str(type(self).__name__),
                out = outpath,
                exception = e
            )
            raise ShoulderGeneratorException(msg)

    @license
    @include_guard
    @header_depends
    def _generate(self, outfile, objects):
        for obj in objects:
            if(isinstance(obj, Register)):
                if not obj.is_sysreg: return

                logger.debug("Writing register: " + str(obj.name))
                self._generate_register(outfile, obj)
            else:
                msg = "Cannot generate object of unsupported {t} type".format(
                    t = type(obj)
                )
                raise ShoulderGeneratorException(msg)

    def _generate_register(self, outfile, reg):
        self._generate_register_comment(outfile, reg)
        self._generate_sysreg_get(outfile, reg)
        if reg.is_writable:
            self._generate_sysreg_set(outfile, reg)

        outfile.write("\n")
        self._generate_register_fieldsets(outfile, reg)

    def _generate_register_fieldsets(self, outfile, reg):
        if not reg.is_sysreg: return

        fieldsets = reg.fieldsets
        if len(fieldsets) == 1:
            self._generate_fieldset(outfile, reg, fieldsets[0])
        elif len(fieldsets) > 1:
            for idx, fieldset in enumerate(fieldsets):
                self._generate_fieldset_comment(outfile, fieldset)
                temp = reg.name
                reg.name = reg.name + "_fieldset_" + str(idx + 1)
                self._generate_fieldset(outfile, reg, fieldset)
                reg.name = temp
        else:
            logger.debug("No fieldsets generated for system register " + str(reg.name))

    def _generate_fieldset(self, outfile, reg, fieldset):
        for field in fieldset.fields:
            if(field.msb == field.lsb):
                self._generate_bitfield_accessors(outfile, reg, field)
            else:
                self._generate_field_accessors(outfile, reg, field)
            outfile.write("\n")

    def _generate_field_accessors(self, outfile, reg, field):
        self._generate_sysreg_register_field_read(outfile, reg, field)
        self._generate_value_register_field_read(outfile, reg, field)
        if reg.is_writable:
            self._generate_sysreg_register_field_write(outfile, reg, field)
            self._generate_value_register_field_write(outfile, reg, field)

    def _generate_bitfield_accessors(self, outfile, reg, field):
        self._generate_sysreg_is_bit_set(outfile, reg, field)
        self._generate_value_is_bit_set(outfile, reg, field)
        self._generate_sysreg_is_bit_cleared(outfile, reg, field)
        self._generate_value_is_bit_cleared(outfile, reg, field)
        if reg.is_writable:
            self._generate_sysreg_bit_set(outfile, reg, field)
            self._generate_value_bit_set(outfile, reg, field)
            self._generate_sysreg_bit_clear(outfile, reg, field)
            self._generate_value_bit_clear(outfile, reg, field)

    def _generate_register_comment(self, outfile, reg):
        reg_comment = "// {name} ({long_name})\n// {purpose}\n".format(
            name = str(reg.name),
            long_name = str(reg.long_name),
            purpose = str(reg.purpose)
        )
        outfile.write(reg_comment)

    def _generate_fieldset_comment(self, outfile, fieldset):
        if(fieldset.condition is not None):
            fieldset_comment = "\t// Fieldset valid when: {comment}\n".format(
                    comment = str(fieldset.condition)
                )
            outfile.write(fieldset_comment)

    def _generate_sysreg_get(self, outfile, reg):
        access_name = str(reg.access_attributes.mnemonic).lower()
        if config.encoded_functions:
            access_name = hex(reg.access_attributes.sysreg_get_encoding())

        reg_getter = "inline {size_t} {c_prefix}{c_suffix}_{regname}_{funcname}(void) "
        reg_getter += "{{ GET_SYSREG_FUNC({accessname}) }}\n"
        reg_getter = reg_getter.format(
            size_t = "uint" + str(reg.size) + "_t",
            c_prefix = config.c_prefix,
            c_suffix = str(reg.size),
            regname = str(reg.name).lower(),
            funcname = config.register_read_function,
            accessname = access_name
        )
        outfile.write(reg_getter)

    def _generate_sysreg_set(self, outfile, reg):
        access_name = str(reg.access_attributes.mnemonic).lower()
        if config.encoded_functions:
            access_name = hex(reg.access_attributes.sysreg_set_encoding())

        reg_setter = "inline void {c_prefix}{c_suffix}_{regname}_{funcname}({size_t} val) "
        reg_setter += "{{ SET_SYSREG_BY_VALUE_FUNC({accessname}, val) }}\n"
        reg_setter = reg_setter.format(
            c_prefix = config.c_prefix,
            c_suffix = str(reg.size),
            regname = str(reg.name).lower(),
            funcname = config.register_write_function,
            size_t = "uint" + str(reg.size) + "_t",
            accessname = access_name
        )
        outfile.write(reg_setter)

    def _generate_sysreg_is_bit_set(self, outfile, reg, field):
        access_name = str(reg.access_attributes.mnemonic).lower()
        if config.encoded_functions:
            access_name = hex(reg.access_attributes.sysreg_get_encoding())

        accessor = "\tinline {size_t} {c_prefix}{c_suffix}_{regname}_{fieldname}_{func}() "
        accessor += "{{ IS_SYSREG_BIT_ENABLED_FUNC({accessname}, {msb}) }}\n"
        accessor = accessor.format(
            size_t = "uint" + str(reg.size) + "_t",
            c_prefix = config.c_prefix,
            c_suffix = str(reg.size),
            regname = str(reg.name).lower(),
            fieldname = str(field.name).lower(),
            func = config.is_bit_set_function,
            accessname = access_name,
            msb = field.msb
        )
        outfile.write(accessor)

    def _generate_value_is_bit_set(self, outfile, reg, field):
        accessor = "\tinline {size_t} {c_prefix}{c_suffix}_{regname}_{fieldname}_{func}_val({size_t} {arg}) "
        accessor += "{{ IS_BIT_ENABLED_FUNC({arg}, {msb}) }}\n"
        accessor = accessor.format(
            size_t = "uint" + str(reg.size) + "_t",
            c_prefix = config.c_prefix,
            c_suffix = str(reg.size),
            regname = str(reg.name).lower(),
            fieldname = str(field.name).lower(),
            func = config.is_bit_set_function,
            arg = str(reg.access_attributes.mnemonic).lower() + "_val",
            msb = field.msb
        )
        outfile.write(accessor)

    def _generate_sysreg_is_bit_cleared(self, outfile, reg, field):
        access_name = str(reg.access_attributes.mnemonic).lower()
        if config.encoded_functions:
            access_name = hex(reg.access_attributes.sysreg_get_encoding())

        accessor = "\tinline {size_t} {c_prefix}{c_suffix}_{regname}_{fieldname}_{func}() "
        accessor += "{{ IS_SYSREG_BIT_DISABLED_FUNC({accessname}, {msb}) }}\n"
        accessor = accessor.format(
            size_t = "uint" + str(reg.size) + "_t",
            c_prefix = config.c_prefix,
            c_suffix = str(reg.size),
            regname = str(reg.name).lower(),
            fieldname = str(field.name).lower(),
            func = config.is_bit_cleared_function,
            accessname = access_name,
            msb = field.msb
        )
        outfile.write(accessor)

    def _generate_value_is_bit_cleared(self, outfile, reg, field):
        accessor = "\tinline {size_t} {c_prefix}{c_suffix}_{regname}_{fieldname}_{func}_val({size_t} {arg}) "
        accessor += "{{ IS_BIT_DISABLED_FUNC({arg}, {msb}) }}\n"
        accessor = accessor.format(
            size_t = "uint" + str(reg.size) + "_t",
            c_prefix = config.c_prefix,
            c_suffix = str(reg.size),
            regname = str(reg.name).lower(),
            fieldname = str(field.name).lower(),
            func = config.is_bit_cleared_function,
            arg = str(reg.access_attributes.mnemonic).lower() + "_val",
            msb = field.msb
        )
        outfile.write(accessor)

    def _generate_sysreg_bit_set(self, outfile, reg, field):
        mask_val = 0
        mask = ""

        for i in range(field.lsb, field.msb + 1):
            mask_val |= 1 << i

        if reg.size == 32:
            mask = "{0:#0{1}x}".format(mask_val, 10)
        else:
            mask = "{0:#0{1}x}".format(mask_val, 18)

        accessor = "\tinline void {c_prefix}{c_suffix}_{regname}_{fieldname}_{func}() "
        accessor = accessor.format(
            c_prefix = config.c_prefix,
            c_suffix = str(reg.size),
            regname = str(reg.name).lower(),
            fieldname = str(field.name).lower(),
            func = config.bit_set_function,
        )

        if config.encoded_functions:
            accessor += "{{ SET_SYSREG_BITS_BY_MASK_FUNC({get_func}, {set_func}, {mask}) }}\n"
            accessor = accessor.format(
                get_func = hex(reg.access_attributes.sysreg_get_encoding()),
                set_func = hex(reg.access_attributes.sysreg_set_encoding()),
                mask = mask
            )
        else:
            accessor += "{{ SET_SYSREG_BITS_BY_MASK_FUNC({accessname}, {mask}) }}\n"
            accessor = accessor.format(
                accessname = str(reg.access_attributes.mnemonic).lower(),
                mask = mask
            )
        outfile.write(accessor)

    def _generate_value_bit_set(self, outfile, reg, field):
        mask_val = 0
        mask = ""

        for i in range(field.lsb, field.msb + 1):
            mask_val |= 1 << i

        if reg.size == 32:
            mask = "{0:#0{1}x}".format(mask_val, 10)
        else:
            mask = "{0:#0{1}x}".format(mask_val, 18)

        accessor = "\tinline {size_t} {c_prefix}{c_suffix}_{regname}_{fieldname}_{func}_val({size_t} {arg}) "
        accessor += "{{ SET_BITS_BY_MASK_FUNC({arg}, {mask}) }}\n"
        accessor = accessor.format(
            size_t = "uint" + str(reg.size) + "_t",
            c_prefix = config.c_prefix,
            c_suffix = str(reg.size),
            regname = str(reg.name).lower(),
            fieldname = str(field.name).lower(),
            func = config.bit_set_function,
            arg = str(reg.access_attributes.mnemonic).lower() + "_val",
            mask = mask
        )
        outfile.write(accessor)

    def _generate_sysreg_bit_clear(self, outfile, reg, field):
        mask_val = 0
        mask = ""

        for i in range(field.lsb, field.msb + 1):
            mask_val |= 1 << i

        if reg.size == 32:
            mask = "{0:#0{1}x}".format(mask_val, 10)
        else:
            mask = "{0:#0{1}x}".format(mask_val, 18)

        accessor = "\tinline void {c_prefix}{c_suffix}_{regname}_{fieldname}_{func}() "
        accessor = accessor.format(
            c_prefix = config.c_prefix,
            c_suffix = str(reg.size),
            regname = str(reg.name).lower(),
            fieldname = str(field.name).lower(),
            func = config.bit_clear_function,
        )

        if config.encoded_functions:
            accessor += "{{ CLEAR_SYSREG_BITS_BY_MASK_FUNC({get_func}, {set_func}, {mask}) }}\n"
            accessor = accessor.format(
                get_func = hex(reg.access_attributes.sysreg_get_encoding()),
                set_func = hex(reg.access_attributes.sysreg_set_encoding()),
                mask = mask
            )
        else:
            accessor += "{{ CLEAR_SYSREG_BITS_BY_MASK_FUNC({accessname}, {mask}) }}\n"
            accessor = accessor.format(
                accessname = str(reg.access_attributes.mnemonic).lower(),
                mask = mask
            )
        outfile.write(accessor)

    def _generate_value_bit_clear(self, outfile, reg, field):
        mask_val = 0
        mask = ""

        for i in range(field.lsb, field.msb + 1):
            mask_val |= 1 << i

        if reg.size == 32:
            mask = "{0:#0{1}x}".format(mask_val, 10)
        else:
            mask = "{0:#0{1}x}".format(mask_val, 18)

        accessor = "\tinline {size_t} {c_prefix}{c_suffix}_{regname}_{fieldname}_{func}_val({size_t} {arg}) "
        accessor += "{{ CLEAR_BITS_BY_MASK_FUNC({arg}, {mask}) }}\n"
        accessor = accessor.format(
            size_t = "uint" + str(reg.size) + "_t",
            c_prefix = config.c_prefix,
            c_suffix = str(reg.size),
            regname = str(reg.name).lower(),
            fieldname = str(field.name).lower(),
            func = config.bit_clear_function,
            arg = str(reg.access_attributes.mnemonic).lower() + "_val",
            mask = mask
        )
        outfile.write(accessor)

    def _generate_sysreg_register_field_read(self, outfile, reg, field):
        mask_val = 0
        mask = ""

        for i in range(field.lsb, field.msb + 1):
            mask_val |= 1 << i

        if reg.size == 32:
            mask = "{0:#0{1}x}".format(mask_val, 10)
        else:
            mask = "{0:#0{1}x}".format(mask_val, 18)

        access_name = str(reg.access_attributes.mnemonic).lower()
        if config.encoded_functions:
            access_name = hex(reg.access_attributes.sysreg_get_encoding())

        accessor = "\tinline {size_t} {c_prefix}{c_suffix}_{regname}_{fieldname}_{func}() "
        accessor += "{{ GET_SYSREG_FIELD_FUNC({accessname}, {mask}, {lsb}) }}\n"
        accessor = accessor.format(
            size_t = "uint" + str(reg.size) + "_t",
            c_prefix = config.c_prefix,
            c_suffix = str(reg.size),
            regname = str(reg.name).lower(),
            fieldname = str(field.name).lower(),
            func = config.register_field_read_function,
            accessname = access_name,
            mask = mask,
            lsb = field.lsb
        )
        outfile.write(accessor)

    def _generate_value_register_field_read(self, outfile, reg, field):
        mask_val = 0
        mask = ""

        for i in range(field.lsb, field.msb + 1):
            mask_val |= 1 << i

        if reg.size == 32:
            mask = "{0:#0{1}x}".format(mask_val, 10)
        else:
            mask = "{0:#0{1}x}".format(mask_val, 18)

        accessor = "\tinline {size_t} {c_prefix}{c_suffix}_{regname}_{fieldname}_{func}_val({size_t} {arg}) "
        accessor += "{{ GET_BITFIELD_FUNC({arg}, {mask}, {lsb}) }}\n"
        accessor = accessor.format(
            size_t = "uint" + str(reg.size) + "_t",
            c_prefix = config.c_prefix,
            c_suffix = str(reg.size),
            regname = str(reg.name).lower(),
            fieldname = str(field.name).lower(),
            func = config.register_field_read_function,
            arg = str(reg.access_attributes.mnemonic).lower() + "_val",
            mask = mask,
            lsb = field.lsb
        )
        outfile.write(accessor)

    def _generate_sysreg_register_field_write(self, outfile, reg, field):
        mask_val = 0
        mask = ""

        for i in range(field.lsb, field.msb + 1):
            mask_val |= 1 << i

        if reg.size == 32:
            mask = "{0:#0{1}x}".format(mask_val, 10)
        else:
            mask = "{0:#0{1}x}".format(mask_val, 18)

        accessor = "\tinline void {c_prefix}{c_suffix}_{regname}_{fieldname}_{func}({size_t} {arg}) "
        accessor = accessor.format(
            c_prefix = config.c_prefix,
            c_suffix = str(reg.size),
            regname = str(reg.name).lower(),
            fieldname = str(field.name).lower(),
            size_t = "uint" + str(reg.size) + "_t",
            func = config.register_field_write_function,
            arg = "value"
        )

        if config.encoded_functions:
            accessor += "{{ SET_SYSREG_BITS_BY_VALUE_FUNC({get_func}, {set_func}, {arg}, {mask}, {lsb}) }}\n"
            accessor = accessor.format(
                get_func = hex(reg.access_attributes.sysreg_get_encoding()),
                set_func = hex(reg.access_attributes.sysreg_set_encoding()),
                arg = "value",
                mask = mask,
                lsb = field.lsb
            )
        else:
            accessor += "{{ SET_SYSREG_BITS_BY_VALUE_FUNC({accessname}, {arg}, {mask}, {lsb}) }}\n"
            accessor = accessor.format(
                accessname = str(reg.access_attributes.mnemonic).lower(),
                arg = "value",
                mask = mask,
                lsb = field.lsb
            )

        outfile.write(accessor)

    def _generate_value_register_field_write(self, outfile, reg, field):
        mask_val = 0
        mask = ""

        for i in range(field.lsb, field.msb + 1):
            mask_val |= 1 << i

        if reg.size == 32:
            mask = "{0:#0{1}x}".format(mask_val, 10)
        else:
            mask = "{0:#0{1}x}".format(mask_val, 18)

        accessor = "\tinline {size_t} {c_prefix}{c_suffix}_{regname}_{fieldname}_{func}_val({size_t} {arg1}, {size_t} {arg2}) "
        accessor += "{{ SET_BITS_BY_VALUE_FUNC({arg1}, {arg2}, {mask}, {lsb}) }}\n"
        accessor = accessor.format(
            size_t = "uint" + str(reg.size) + "_t",
            c_prefix = config.c_prefix,
            c_suffix = str(reg.size),
            regname = str(reg.name).lower(),
            fieldname = str(field.name).lower(),
            func = config.register_field_write_function,
            arg1 = str(reg.access_attributes.mnemonic).lower(),
            arg2 = "value",
            mask = mask,
            lsb = field.lsb
        )
        outfile.write(accessor)
