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

class CxxHeaderGenerator(AbstractGenerator):

    def generate(self, objects, outpath):
        try:
            outfile_path = os.path.abspath(os.path.join(outpath, "shoulder.h"))
            logger.info("Generating C++ header: " + str(outfile_path))
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
    @cxx.namespace(name=config.cxx_namespace)
    def _generate(self, outfile, objects):
        """
        Generate for all objects passed into this generator.  Wrap all generated
        content in a license, include guard, and namespace. Append low-level
        accessor macros before generating register accessors
        """
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
        """
        Generate accessors for a single register
        """
        self._generate_register_comment(outfile, reg)

        @cxx.namespace(name=str(reg.name).lower())
        def _in_register_namespace(self, outfile, reg):
            if reg.size == 32:
                self._generate_sysreg_32_get(outfile, reg)
                self._generate_sysreg_32_set(outfile, reg)

            else:
                self._generate_sysreg_64_get(outfile, reg)
                self._generate_sysreg_64_set(outfile, reg)

            self._generate_register_fieldsets(outfile, reg)

        _in_register_namespace(self, outfile, reg)

    def _generate_register_fieldsets(self, outfile, reg):
        """
        Generate accessors for all fieldsets that belong to a register
        """
        fieldsets = reg.fieldsets

        if len(fieldsets) == 1:
            self._generate_fieldset(outfile, reg, fieldsets[0])

        elif len(fieldsets) > 1:
            for idx, fieldset in enumerate(fieldsets):
                self._generate_fieldset_comment(outfile, fieldset)

                @cxx.namespace(name="fieldset_" + str(idx), indent=1)
                def _in_fieldset_namespace(self, outfile, reg, fieldset):
                    self._generate_fieldset(outfile, reg, fieldset)

                _in_fieldset_namespace(self, outfile, reg, fieldset)
        else:
            logger.debug("No fieldsets generated for system register " + str(reg.name))

    def _generate_fieldset(self, outfile, reg, fieldset):
        """
        Generate accessors for a single register fieldset
        """
        for field in fieldset.fields:

            @cxx.namespace(name=str(field.name).lower(), indent=1)
            def _in_field_namespace(self, outfile):
                self._generate_field_constants(outfile, reg, field)

                if(field.msb == field.lsb):
                    self._generate_bitfield_accessors(outfile, reg, field)

                else:
                    self._generate_field_accessors(outfile, reg, field)

            _in_field_namespace(self, outfile)

    def _generate_field_constants(self, outfile, reg, field):
        """
        Generate constants for a field (i.e. mask, msb, lsb)
        """
        field_prefix = "\t\tconstexpr "
        mask_val = 0

        for i in range(field.lsb, field.msb + 1):
            mask_val |= 1 << i

        if reg.size == 32:
            mask = "{0:#0{1}x}".format(mask_val, 10)
            outfile.write(field_prefix + "uint32_t mask = " + str(mask) + ";\n")
            outfile.write(field_prefix + "uint32_t msb  = " + str(field.msb) + ";\n")
            outfile.write(field_prefix + "uint32_t lsb  = " + str(field.lsb) + ";\n")
            outfile.write("\n")

        else:
            mask = "{0:#0{1}x}".format(mask_val, 18)
            outfile.write(field_prefix + "uint64_t mask = " + str(mask) + ";\n")
            outfile.write(field_prefix + "uint64_t msb  = " + str(field.msb) + ";\n")
            outfile.write(field_prefix + "uint64_t lsb  = " + str(field.lsb) + ";\n")
            outfile.write("\n")

    def _generate_field_accessors(self, outfile, reg, field):
        """
        Generate accessors for a field (i.e. larger than a single bit)
        """
        if reg.size == 32:
            self._generate_sysreg_32_register_field_read(outfile, reg, field)
            self._generate_value_32_register_field_read(outfile, reg, field)
            self._generate_sysreg_32_register_field_write(outfile, reg, field)
            self._generate_value_32_register_field_write(outfile, reg, field)

        else:
            self._generate_sysreg_64_register_field_read(outfile, reg, field)
            self._generate_value_64_register_field_read(outfile, reg, field)
            self._generate_sysreg_64_register_field_write(outfile, reg, field)
            self._generate_value_64_register_field_write(outfile, reg, field)

    def _generate_bitfield_accessors(self, outfile, reg, field):
        """
        Generate accessors for a bitfield (i.e. a single bit)
        """
        if reg.size == 32:
            self._generate_sysreg_32_is_bit_set(outfile, reg, field)
            self._generate_value_32_is_bit_set(outfile, reg, field)
            self._generate_sysreg_32_is_bit_cleared(outfile, reg, field)
            self._generate_value_32_is_bit_cleared(outfile, reg, field)
            self._generate_sysreg_32_bit_set(outfile, reg, field)
            self._generate_value_32_bit_set(outfile, reg, field)
            self._generate_sysreg_32_bit_clear(outfile, reg, field)
            self._generate_value_32_bit_clear(outfile, reg, field)

        else:
            self._generate_sysreg_64_is_bit_set(outfile, reg, field)
            self._generate_value_64_is_bit_set(outfile, reg, field)
            self._generate_sysreg_64_is_bit_cleared(outfile, reg, field)
            self._generate_value_64_is_bit_cleared(outfile, reg, field)
            self._generate_sysreg_64_bit_set(outfile, reg, field)
            self._generate_value_64_bit_set(outfile, reg, field)
            self._generate_sysreg_64_bit_clear(outfile, reg, field)
            self._generate_value_64_bit_clear(outfile, reg, field)

    def _generate_register_comment(self, outfile, reg):
        """
        Generate a comment for a register
        """
        reg_comment = "// {name} ({long_name})\n// {purpose}\n".format(
            name = str(reg.name),
            long_name = str(reg.long_name),
            purpose = str(reg.purpose)
        )
        outfile.write(reg_comment)

    def _generate_fieldset_comment(self, outfile, fieldset):
        """
        Generate a comment for a fieldset
        """
        if(fieldset.condition is not None):
            fieldset_comment = "\t// Fieldset valid when: {comment}\n".format(
                comment = str(fieldset.condition)
            )
            outfile.write(fieldset_comment)

    @cxx.get_32(indent=1)
    def _generate_sysreg_32_get(self, outfile, reg):
        """
        Generate a function that reads a 32-bit system register directly
        """
        outfile.write("GET_SYSREG_FUNC(" + str(reg.name).lower() + ")")

    @cxx.get_64(indent=1)
    def _generate_sysreg_64_get(self, outfile, reg):
        """
        Generate a function that reads a 64-bit system register directly
        """
        outfile.write("GET_SYSREG_FUNC(" + str(reg.name).lower() + ")")

    @cxx.set_32(indent=1)
    def _generate_sysreg_32_set(self, outfile, reg):
        """
        Generate a function that writes to a 32-bit system register directly
        """
        outfile.write("SET_SYSREG_BY_VALUE_FUNC(" + str(reg.name).lower() + ", val)")

    @cxx.set_64(indent=1)
    def _generate_sysreg_64_set(self, outfile, reg):
        """
        Generate a function that writes to a 64-bit system register directly
        """
        outfile.write("SET_SYSREG_BY_VALUE_FUNC(" + str(reg.name).lower() + ", val)")

    @cxx.get_32(indent=2, name=str(config.is_bit_set_function))
    def _generate_sysreg_32_is_bit_set(self, outfile, reg, field):
        """
        Generate a function that checks if a bit is enabled by reading from a
        32-bit system register directly
        """
        outfile.write("IS_SYSREG_BIT_ENABLED_FUNC(")
        outfile.write(str(reg.name).lower())
        outfile.write(", lsb)")

    @cxx.get_64(indent=2, name=str(config.is_bit_set_function))
    def _generate_sysreg_64_is_bit_set(self, outfile, reg, field):
        """
        Generate a function that checks if a bit is enabled by reading from a
        64-bit system register directly
        """
        outfile.write("IS_SYSREG_BIT_ENABLED_FUNC(")
        outfile.write(str(reg.name).lower())
        outfile.write(", lsb)")

    @cxx.get_32_from_value(indent=2, name=str(config.is_bit_set_function))
    def _generate_value_32_is_bit_set(self, outfile, reg, field):
        """
        Generate a function that checks if a bit is enabled by reading from a
        32-bit integer value
        """
        outfile.write("IS_BIT_ENABLED_FUNC(val, lsb)")

    @cxx.get_64_from_value(indent=2, name=str(config.is_bit_set_function))
    def _generate_value_64_is_bit_set(self, outfile, reg, field):
        """
        Generate a function that checks if a bit is enabled by reading from a
        64-bit integer value
        """
        outfile.write("IS_BIT_ENABLED_FUNC(val, lsb)")

    @cxx.get_32(indent=2, name=str(config.is_bit_cleared_function))
    def _generate_sysreg_32_is_bit_cleared(self, outfile, reg, field):
        """
        Generate a function that checks if a bit is disabled by reading from a
        32-bit system register directly
        """
        outfile.write("IS_SYSREG_BIT_DISABLED_FUNC(")
        outfile.write(str(reg.name).lower())
        outfile.write(", lsb)")

    @cxx.get_64(indent=2, name=str(config.is_bit_cleared_function))
    def _generate_sysreg_64_is_bit_cleared(self, outfile, reg, field):
        """
        Generate a function that checks if a bit is disabled by reading from a
        64-bit system register directly
        """
        outfile.write("IS_SYSREG_BIT_DISABLED_FUNC(")
        outfile.write(str(reg.name).lower())
        outfile.write(", lsb)")

    @cxx.get_32_from_value(indent=2, name=str(config.is_bit_cleared_function))
    def _generate_value_32_is_bit_cleared(self, outfile, reg, field):
        """
        Generate a function that checks if a bit is disabled by reading from a
        32-bit integer value
        """
        outfile.write("IS_BIT_DISABLED_FUNC(val, lsb)")

    @cxx.get_64_from_value(indent=2, name=str(config.is_bit_cleared_function))
    def _generate_value_64_is_bit_cleared(self, outfile, reg, field):
        """
        Generate a function that checks if a bit is disabled by reading from a
        64-bit integer value
        """
        outfile.write("IS_BIT_DISABLED_FUNC(val, lsb)")

    @cxx.set_constant(indent=2, name=str(config.bit_set_function))
    def _generate_sysreg_32_bit_set(self, outfile, reg, field):
        """
        Generate a function that enables a bit by writing to a 32-bit system
        register directly
        """
        outfile.write("SET_SYSREG_BITS_BY_MASK_FUNC(")
        outfile.write(str(reg.name).lower())
        outfile.write(", mask)")

    @cxx.set_constant(indent=2, name=str(config.bit_set_function))
    def _generate_sysreg_64_bit_set(self, outfile, reg, field):
        """
        Generate a function that enables a bit by writing to a 64-bit system
        register directly
        """
        outfile.write("SET_SYSREG_BITS_BY_MASK_FUNC(")
        outfile.write(str(reg.name).lower())
        outfile.write(", mask)")

    @cxx.get_32_from_value(indent=2, name=str(config.bit_set_function))
    def _generate_value_32_bit_set(self, outfile, reg, field):
        """
        Generate a function that enables a bit by writing to a 32-bit integer
        value
        """
        outfile.write("SET_BITS_BY_MASK_FUNC(val, mask)")

    @cxx.get_64_from_value(indent=2, name=str(config.bit_set_function))
    def _generate_value_64_bit_set(self, outfile, reg, field):
        """
        Generate a function that enables a bit by writing to a 64-bit integer
        value
        """
        outfile.write("SET_BITS_BY_MASK_FUNC(val, mask)")

    @cxx.set_constant(indent=2, name=str(config.bit_clear_function))
    def _generate_sysreg_32_bit_clear(self, outfile, reg, field):
        """
        Generate a function that disables a bit by writing to a 32-bit system
        register directly
        """
        outfile.write("CLEAR_SYSREG_BITS_BY_MASK_FUNC(")
        outfile.write(str(reg.name).lower())
        outfile.write(", mask)")

    @cxx.set_constant(indent=2, name=str(config.bit_clear_function))
    def _generate_sysreg_64_bit_clear(self, outfile, reg, field):
        """
        Generate a function that disables a bit by writing to a 64-bit system
        register directly
        """
        outfile.write("CLEAR_SYSREG_BITS_BY_MASK_FUNC(")
        outfile.write(str(reg.name).lower())
        outfile.write(", mask)")

    @cxx.get_32_from_value(indent=2, name=str(config.bit_clear_function))
    def _generate_value_32_bit_clear(self, outfile, reg, field):
        """
        Generate a function that disables a bit by writing to a 32-bit integer
        value
        """
        outfile.write("CLEAR_BITS_BY_MASK_FUNC(val, mask)")

    @cxx.get_64_from_value(indent=2, name=str(config.bit_clear_function))
    def _generate_value_64_bit_clear(self, outfile, reg, field):
        """
        Generate a function that disables a bit by writing to a 64-bit integer
        value
        """
        outfile.write("CLEAR_BITS_BY_MASK_FUNC(val, mask)")

    @cxx.get_32(indent=2, name=str(config.register_field_read_function))
    def _generate_sysreg_32_register_field_read(self, outfile, reg, field):
        """
        Generate a function that gets a field value by reading from a 32-bit
        system register directly
        """
        outfile.write("GET_SYSREG_FIELD_FUNC(")
        outfile.write(str(reg.name).lower())
        outfile.write(", mask, lsb)")

    @cxx.get_64(indent=2, name=str(config.register_field_read_function))
    def _generate_sysreg_64_register_field_read(self, outfile, reg, field):
        """
        Generate a function that gets a field value by reading from a 64-bit
        system register directly
        """
        outfile.write("GET_SYSREG_FIELD_FUNC(")
        outfile.write(str(reg.name).lower())
        outfile.write(", mask, lsb)")

    @cxx.get_32_from_value(indent=2, name=str(config.register_field_read_function))
    def _generate_value_32_register_field_read(self, outfile, reg, field):
        """
        Generate a function that gets a field value by reading from a 32-bit
        integer value
        """
        outfile.write("GET_BITFIELD_FUNC(val, mask, lsb)")

    @cxx.get_64_from_value(indent=2, name=str(config.register_field_read_function))
    def _generate_value_64_register_field_read(self, outfile, reg, field):
        """
        Generate a function that gets a field value by reading from a 64-bit
        integer value
        """
        outfile.write("GET_BITFIELD_FUNC(val, mask, lsb)")

    @cxx.set_32(indent=2, name=str(config.register_field_write_function))
    def _generate_sysreg_32_register_field_write(self, outfile, reg, field):
        """
        Generate a function that sets a field value by writing to a 32-bit
        system register directly
        """
        outfile.write("GET_SYSREG_FIELD_FUNC(")
        outfile.write(str(reg.name).lower())
        outfile.write(", mask, lsb)")

    @cxx.set_64(indent=2, name=str(config.register_field_write_function))
    def _generate_sysreg_64_register_field_write(self, outfile, reg, field):
        """
        Generate a function that sets a field value by writing to a 64-bit
        system register directly
        """
        outfile.write("GET_SYSREG_FIELD_FUNC(")
        outfile.write(str(reg.name).lower())
        outfile.write(", mask, lsb)")

    @cxx.set_32_to_value(indent=2, name=str(config.register_field_write_function))
    def _generate_value_32_register_field_write(self, outfile, reg, field):
        """
        Generate a function that sets a field value by writing to a 32-bit
        integer value
        """
        outfile.write("SET_BITS_BY_VALUE_FUNC(val, fieldval, mask, lsb)")

    @cxx.set_64_to_value(indent=2, name=str(config.register_field_write_function))
    def _generate_value_64_register_field_write(self, outfile, reg, field):
        """
        Generate a function that sets a field value by writing to a 64-bit
        integer value
        """
        outfile.write("SET_BITS_BY_VALUE_FUNC(val, fieldval, mask, lsb)")
