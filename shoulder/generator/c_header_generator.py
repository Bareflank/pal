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
import textwrap

from shoulder.generator.abstract_generator import AbstractGenerator
from shoulder.logger import logger
from shoulder.config import config
from shoulder.exception import ShoulderGeneratorException
from shoulder.filter import filters
from shoulder.transform import transforms
import shoulder.gadget


class CHeaderGenerator(AbstractGenerator):
    def generate(self, regs, outpath):
        try:
            outfile_path = os.path.abspath(os.path.join(outpath, "shoulder.h"))
            logger.info("Generating C Header: " + str(outfile_path))

            regs = transforms["remove_reserved_0"].transform(regs)
            regs = transforms["remove_reserved_1"].transform(regs)
            regs = transforms["remove_reserved_sign_extended"].transform(regs)
            regs = transforms["remove_implementation_defined"].transform(regs)
            regs = transforms["special_to_underscore"].transform(regs)
            regs = transforms["remove_redundant_am"].transform(regs)
            regs = transforms["remove_redundant_fields"].transform(regs)
            regs = transforms["unique_fieldset_names"].transform(regs)

            regs = filters["no_access_mechanism"].filter_exclusive(regs)

            if config.encoded_functions:
                msg = "Encoded accessors are only supported for aarch64 "
                msg += "registers (aarch32 and external not supported)"
                logger.warn(msg)
                regs = filters["aarch64"].filter_inclusive(regs)

            self.gadgets["shoulder.header_depends"].includes = [
                "<stdint.h>",
                "aarch32_gcc_accessor_macros.h",
                "aarch64_gcc_accessor_macros.h"
            ]

            unique = []
            for reg in regs:
                external_mechs = reg.access_mechanisms["ldr"] + \
                                 reg.access_mechanisms["str"]
                for mech in external_mechs:
                    if mech.component not in unique:
                        unique.append(mech.component)
            self.gadgets["shoulder.external_component"].components = unique

            with open(outfile_path, "w") as outfile:
                self._generate(outfile, regs)

        except Exception as e:
            msg = "{g} failed to generate output {out}: {exception}".format(
                g=str(type(self).__name__),
                out=outpath,
                exception=e)
            raise ShoulderGeneratorException(msg)

    @shoulder.gadget.license
    @shoulder.gadget.include_guard
    @shoulder.gadget.header_depends
    @shoulder.gadget.external_component
    def _generate(self, outfile, regs):

        for reg in regs:
            self.gadgets["shoulder.c.enum"].indent = 0
            self.gadgets["shoulder.c.function_definition"].indent = 0

            self._generate_register_comment(outfile, reg)
            self._generate_register_get(outfile, reg)
            self._generate_register_set(outfile, reg)

            self.gadgets["shoulder.c.enum"].indent = 1
            self.gadgets["shoulder.c.function_definition"].indent = 1

            for idx, fieldset in enumerate(reg.fieldsets):
                self._generate_fieldset_comment(outfile, fieldset, idx + 1)

                for field in fieldset.fields:
                    self._generate_field_constants(outfile, reg, field)
                    if field.msb == field.lsb:
                        self._generate_bitfield_set(outfile, reg, field)
                        self._generate_bitfield_set_val(outfile, reg, field)
                        self._generate_bitfield_is_set(outfile, reg, field)
                        self._generate_bitfield_is_set_val(outfile, reg, field)
                        self._generate_bitfield_clear(outfile, reg, field)
                        self._generate_bitfield_clear_val(outfile, reg, field)
                        self._generate_bitfield_is_clear(outfile, reg, field)
                        self._generate_bitfield_is_clear_val(outfile, reg, field)
                    else:
                        self._generate_field_get(outfile, reg, field)
                        self._generate_field_get_val(outfile, reg, field)
                        self._generate_field_set(outfile, reg, field)
                        self._generate_field_set_val(outfile, reg, field)

    def _generate_register_comment(self, outfile, reg):
        comment = "// {name} ({long_name})\n".format(
            name=str(reg.name),
            long_name=str(reg.long_name)
        )
        outfile.write(comment)

        comment = str(reg.purpose)
        wrapped = textwrap.wrap(comment, width=75)
        for line in wrapped:
            line = "// " + str(line) + "\n"
            outfile.write(line)

    def _generate_fieldset_comment(self, outfile, fieldset, idx):
        if fieldset.condition:
            fieldset_comment = "Fieldset {idx}: {comment}\n".format(
                idx=idx,
                comment=str(fieldset.condition)
            )
            wrapped = textwrap.wrap(fieldset_comment, width=71)
            for line in wrapped:
                line = "\t// " + str(line) + "\n"
                outfile.write(line)

# ----------------------------------------------------------------------------
# register_get
# ----------------------------------------------------------------------------

    def _generate_register_get(self, outfile, reg):
        """
        Generate a C function that reads the given register
        """

        if not reg.is_readable():
            return

        rname = reg.name.lower()
        prefix = self._register_function_prefix(reg)
        suffix = config.register_read_function

        gadget = self.gadgets["shoulder.c.function_definition"]
        gadget.name = prefix + "_" + rname + "_" + suffix
        gadget.return_type = self._register_size_type(reg)
        gadget.args = []

        if reg.access_mechanisms["mrs_register"]:
            am = reg.access_mechanisms["mrs_register"][0]
            if config.encoded_functions:
                self._generate_aarch64_encoded_get(outfile, reg, am)
            else:
                self._generate_mrs_register_get(outfile, reg, am)

        elif reg.access_mechanisms["mrs_banked"]:
            am = reg.access_mechanisms["mrs_banked"][0]
            self._generate_mrs_banked_get(outfile, reg, am)

        elif reg.access_mechanisms["mrc"]:
            am = reg.access_mechanisms["mrc"][0]
            self._generate_mrc_get(outfile, reg, am)

        elif reg.access_mechanisms["mrrc"]:
            gadget.return_type = "uint64_t"

            am = reg.access_mechanisms["mrrc"][0]
            self._generate_mrrc_get(outfile, reg, am)

        elif reg.access_mechanisms["vmrs"]:
            am = reg.access_mechanisms["vmrs"][0]
            self._generate_vmrs_get(outfile, reg, am)

        elif reg.access_mechanisms["ldr"]:
            am = reg.access_mechanisms["ldr"][0]
            self._generate_external_constants(outfile, reg, am)
            self._generate_ldr_get(outfile, reg, am)

        else:
            msg = "Failed to generate {f} function for readable register {r}"
            msg = msg.format(
                f=config.register_read_function,
                r=reg.name.lower()
            )
            logger.error(msg)

    @shoulder.gadget.c.function_definition
    def _generate_aarch64_encoded_get(self, outfile, reg, am):
        reg_getter = "SHOULDER_AARCH64_ENCODED_READ_IMPL({encoding})".format(
            encoding=hex(am.binary_encoded())
        )
        outfile.write(reg_getter)

    @shoulder.gadget.c.function_definition
    def _generate_mrs_register_get(self, outfile, reg, am):
        reg_getter = "SHOULDER_AARCH64_MRS_REGISTER_IMPL({mnemonic})".format(
            mnemonic=am.operand_mnemonic.lower()
        )
        outfile.write(reg_getter)

    @shoulder.gadget.c.function_definition
    def _generate_mrs_banked_get(self, outfile, reg, am):
        reg_getter = "SHOULDER_AARCH32_MRS_BANKED_IMPL({mnemonic})".format(
            mnemonic=am.operand_mnemonic.lower()
        )
        outfile.write(reg_getter)

    @shoulder.gadget.c.function_definition
    def _generate_mrc_get(self, outfile, reg, am):
        reg_getter = "SHOULDER_AARCH32_MRC_IMPL({coproc}, {opc1}, {crn}, {crm}, {opc2})"
        reg_getter = reg_getter.format(
            coproc=am.coproc,
            opc1=am.opc1,
            crn=am.crn,
            crm=am.crm,
            opc2=am.opc2
        )

        outfile.write(reg_getter)

    @shoulder.gadget.c.function_definition
    def _generate_mrrc_get(self, outfile, reg, am):
        reg_getter = "SHOULDER_AARCH32_MRRC_IMPL({coproc}, {opc1}, {crm})"
        reg_getter = reg_getter.format(
            coproc=am.coproc,
            opc1=am.opc1,
            crm=am.crm
        )

        outfile.write(reg_getter)

    @shoulder.gadget.c.function_definition
    def _generate_vmrs_get(self, outfile, reg, am):
        reg_getter = "SHOULDER_AARCH32_VMRS_IMPL({key})".format(
            key=am.operand_mnemonic.lower()
        )
        outfile.write(reg_getter)

    @shoulder.gadget.c.function_definition
    def _generate_ldr_get(self, outfile, reg, am):
        null_return = "0xffffffff"
        if reg.size == 64:
            null_return = "0xffffffffffffffff"

        reg_getter =  "if ({base} == 0x0) return {null_ret};\n"
        reg_getter += "return *(({ret_size} *)({base} + {prefix}_{reg}_offset));\n"
        reg_getter = reg_getter.format(
            base=str(am.component) + "_base",
            null_ret=null_return,
            ret_size=self._register_size_type(reg),
            prefix=self._register_function_prefix(reg),
            reg=reg.name.lower()
        )
        outfile.write(reg_getter)

# ----------------------------------------------------------------------------
# register_set
# ----------------------------------------------------------------------------

    def _generate_register_set(self, outfile, reg):
        """
        Generate a C function that writes the given register
        """

        if not reg.is_writeable():
            return

        rname = reg.name.lower()
        prefix = self._register_function_prefix(reg)
        suffix = config.register_write_function
        size_type = self._register_size_type(reg)

        gadget = self.gadgets["shoulder.c.function_definition"]
        gadget.name = prefix + "_" + rname + "_" + suffix
        gadget.return_type = "void"
        gadget.args = [(size_type, "val")]

        if reg.access_mechanisms["msr_register"]:
            am = reg.access_mechanisms["msr_register"][0]
            if config.encoded_functions:
                self._generate_aarch64_encoded_set(outfile, reg, am)
            else:
                self._generate_msr_register_set(outfile, reg, am)

        elif reg.access_mechanisms["mcr"]:
            am = reg.access_mechanisms["mcr"][0]
            self._generate_mcr_set(outfile, reg, am)

        elif reg.access_mechanisms["mcrr"]:
            gadget.args = [("uint64_t", "val")]

            am = reg.access_mechanisms["mcrr"][0]
            self._generate_mcrr_set(outfile, reg, am)

        elif reg.access_mechanisms["msr_banked"]:
            am = reg.access_mechanisms["msr_banked"][0]
            self._generate_msr_banked_set(outfile, reg, am)

        elif reg.access_mechanisms["vmsr"]:
            am = reg.access_mechanisms["vmsr"][0]
            self._generate_vmsr_set(outfile, reg, am)

        elif reg.access_mechanisms["str"]:
            am = reg.access_mechanisms["str"][0]
            if not reg.is_readable():
                self._generate_external_constants(outfile, reg, am)
            self._generate_str_set(outfile, reg, am)

        elif reg.access_mechanisms["msr_immediate"]:
            msg = "MSRimmediate access mechanism not supported for register {r}"
            logger.warn(msg.format(r=reg.name.lower()))

        else:
            msg = "Failed to generate {f} function for writeable register {r}"
            msg = msg.format(
                f=config.register_write_function,
                r=reg.name.lower()
            )
            logger.error(msg)

    @shoulder.gadget.c.function_definition
    def _generate_aarch64_encoded_set(self, outfile, reg, am):
        reg_setter = "SHOULDER_AARCH64_ENCODED_WRITE_IMPL({encoding}, val)".format(
            encoding=hex(am.binary_encoded())
        )
        outfile.write(reg_setter)

    @shoulder.gadget.c.function_definition
    def _generate_msr_register_set(self, outfile, reg, am):
        reg_setter = "SHOULDER_AARCH64_MSR_REGISTER_IMPL({mnemonic}, val)".format(
            mnemonic=am.operand_mnemonic.lower()
        )
        outfile.write(reg_setter)

    @shoulder.gadget.c.function_definition
    def _generate_mcr_set(self, outfile, reg, am):
        reg_setter = "SHOULDER_AARCH32_MCR_IMPL({coproc}, {opc1}, {crn}, {crm}, {opc2}, val)"
        reg_setter = reg_setter.format(
            coproc=am.coproc,
            opc1=am.opc1,
            crn=am.crn,
            crm=am.crm,
            opc2=am.opc2
        )

        outfile.write(reg_setter)

    @shoulder.gadget.c.function_definition
    def _generate_mcrr_set(self, outfile, reg, am):
        reg_setter = "SHOULDER_AARCH32_MCRR_IMPL({coproc}, {opc1}, {crm}, val)"
        reg_setter = reg_setter.format(
            coproc=am.coproc,
            opc1=am.opc1,
            crm=am.crm
        )

        outfile.write(reg_setter)

    @shoulder.gadget.c.function_definition
    def _generate_msr_banked_set(self, outfile, reg, am):
        reg_setter = "SHOULDER_AARCH32_MSR_BANKED_IMPL({mnemonic}, val)".format(
            mnemonic=am.operand_mnemonic.lower()
        )
        outfile.write(reg_setter)

    @shoulder.gadget.c.function_definition
    def _generate_vmsr_set(self, outfile, reg, am):
        reg_setter = "SHOULDER_AARCH32_VMSR_IMPL({key}, val)".format(
            key=am.operand_mnemonic.lower()
        )
        outfile.write(reg_setter)

    @shoulder.gadget.c.function_definition
    def _generate_str_set(self, outfile, reg, am):
        null_return = "0xffffffff"
        if reg.size == 64:
            null_return = "0xffffffffffffffff"

        reg_setter =  "if ({base} == 0x0) return {null_ret};\n"
        reg_setter += "*(({ret_size} *)({base} + {prefix}_{reg}_offset)) = val;\n"
        reg_setter = reg_setter.format(
            base=str(am.component) + "_base",
            null_ret=null_return,
            ret_size=self._register_size_type(reg),
            prefix=self._register_function_prefix(reg),
            reg=reg.name.lower()
        )
        outfile.write(reg_setter)

# ----------------------------------------------------------------------------
# constants
# ----------------------------------------------------------------------------

    @shoulder.gadget.c.enum
    def _generate_external_constants(self, outfile, reg, am):
        """
        Generate constants that describe the address offset of the given register
        """

        constants = "{prefix}_{reg}_offset = {offset}\n"
        constants = constants.format(
            prefix=self._register_function_prefix(reg),
            reg=reg.name.lower(),
            offset=am.offset
        )

        outfile.write(constants)


    @shoulder.gadget.c.enum
    def _generate_field_constants(self, outfile, reg, field):
        """
        Generate constants that describe the given field in the given register
        """

        constants = "{prefix}_{reg}_{field}_lsb = {lsb},\n"
        constants += "{prefix}_{reg}_{field}_msb = {msb},\n"
        constants += "{prefix}_{reg}_{field}_mask = {mask}"
        constants = constants.format(
            prefix=self._register_function_prefix(reg),
            reg=reg.name.lower(),
            field=field.name.lower(),
            lsb=str(field.lsb),
            msb=str(field.msb),
            mask=self._field_mask_hex_string(reg, field)
        )

        outfile.write(constants)

# ----------------------------------------------------------------------------
# bitfield_set
# ----------------------------------------------------------------------------
    def _generate_bitfield_set(self, outfile, reg, field):
        """
        Generate a C function that sets/enables the given bitfield (to 1) in the
        given register
        """

        if reg.is_writeable() and reg.is_readable():
            gadget = self.gadgets["shoulder.c.function_definition"]
            gadget.return_type = "void"
            gadget.args = []
            gadget.name = "{prefix}_{rname}_{fname}_{suffix}".format(
                prefix=self._register_function_prefix(reg),
                rname=reg.name.lower(),
                fname=field.name.lower(),
                suffix=config.bit_set_function
            )

            self._bitfield_set(outfile, reg, field)

    @shoulder.gadget.c.function_definition
    def _bitfield_set(self, outfile, reg, field):
        f_body = "{size} val = {reg_get}();\n"
        f_body += "{reg_set}(val | {mask});"

        f_body = f_body.format(
            size=self._register_size_type(reg),
            mask=self._field_mask_string(reg, field),
            reg_get=self._register_read_function_name(reg),
            reg_set=self._register_write_function_name(reg)
        )

        outfile.write(f_body)

# ----------------------------------------------------------------------------
# bitfield_set_val
# ----------------------------------------------------------------------------
    def _generate_bitfield_set_val(self, outfile, reg, field):
        """
        Generate a C function that sets the given bitfield (1) in an integer
        value
        """

        if reg.is_writeable():
            size_type = self._register_size_type(reg)

            gadget = self.gadgets["shoulder.c.function_definition"]
            gadget.return_type = size_type
            gadget.args = [(size_type, "val")]
            gadget.name = "{prefix}_{rname}_{fname}_{suffix}".format(
                prefix=self._register_function_prefix(reg),
                rname=reg.name.lower(),
                fname=field.name.lower(),
                suffix=config.bit_set_function + "_val"
            )

            self._bitfield_set_val(outfile, reg, field)

    @shoulder.gadget.c.function_definition
    def _bitfield_set_val(self, outfile, reg, field):
        f_body = "return val | {mask};".format(
            mask=self._field_mask_string(reg, field)
        )
        outfile.write(f_body)

# ----------------------------------------------------------------------------
# bitfield_is_set
# ----------------------------------------------------------------------------

    def _generate_bitfield_is_set(self, outfile, reg, field):
        """
        Generate a C function that checks if the given bitfield is set (1) in
        the given register
        """

        if reg.is_readable():
            size_type = self._register_size_type(reg)

            gadget = self.gadgets["shoulder.c.function_definition"]
            gadget.return_type = size_type
            gadget.args = []
            gadget.name = "{prefix}_{rname}_{fname}_{suffix}".format(
                prefix=self._register_function_prefix(reg),
                rname=reg.name.lower(),
                fname=field.name.lower(),
                suffix=config.is_bit_set_function
            )

            self._bitfield_is_set(outfile, reg, field)

    @shoulder.gadget.c.function_definition
    def _bitfield_is_set(self, outfile, reg, field):
        f_body = "{size} val = {reg_get}();\n"
        f_body += "return (val & {mask}) != 0;"

        f_body = f_body.format(
            size=self._register_size_type(reg),
            mask=self._field_mask_string(reg, field),
            reg_get=self._register_read_function_name(reg),
        )

        outfile.write(f_body)

# ----------------------------------------------------------------------------
# bitfield_is_set_val
# ----------------------------------------------------------------------------
    def _generate_bitfield_is_set_val(self, outfile, reg, field):
        """
        Generate a C function that checks if the given bitfield is set/enabled
        (to 1) in an integer value
        """

        if reg.is_readable():
            size_type = self._register_size_type(reg)

            gadget = self.gadgets["shoulder.c.function_definition"]
            gadget.return_type = size_type
            gadget.args = [(size_type, "val")]
            gadget.name = "{prefix}_{rname}_{fname}_{suffix}".format(
                prefix=self._register_function_prefix(reg),
                rname=reg.name.lower(),
                fname=field.name.lower(),
                suffix=config.is_bit_set_function + "_val"
            )

            self._bitfield_is_set_val(outfile, reg, field)

    @shoulder.gadget.c.function_definition
    def _bitfield_is_set_val(self, outfile, reg, field):
        f_body = "return (val & {mask}) != 0;"

        f_body = f_body.format(
            mask=self._field_mask_string(reg, field)
        )

        outfile.write(f_body)

# ----------------------------------------------------------------------------
# bitfield_disable
# ----------------------------------------------------------------------------
    def _generate_bitfield_clear(self, outfile, reg, field):
        """
        Generate a C function that disables the given bitfield (to 1) in the
        given register
        """

        if reg.is_writeable() and reg.is_readable():
            gadget = self.gadgets["shoulder.c.function_definition"]
            gadget.return_type = "void"
            gadget.args = []
            gadget.name = "{prefix}_{rname}_{fname}_{suffix}".format(
                prefix=self._register_function_prefix(reg),
                rname=reg.name.lower(),
                fname=field.name.lower(),
                suffix=config.bit_clear_function
            )

            self._bitfield_clear(outfile, reg, field)

    @shoulder.gadget.c.function_definition
    def _bitfield_clear(self, outfile, reg, field):
        f_body = "{size} val = {reg_get}();\n"
        f_body += "{reg_set}(val & ~{mask});"

        f_body = f_body.format(
            size=self._register_size_type(reg),
            mask=self._field_mask_string(reg, field),
            reg_get=self._register_read_function_name(reg),
            reg_set=self._register_write_function_name(reg)
        )

        outfile.write(f_body)

# ----------------------------------------------------------------------------
# bitfield_clear_val
# ----------------------------------------------------------------------------
    def _generate_bitfield_clear_val(self, outfile, reg, field):
        """
        Generate a C function that clears the given bitfield (1) in an integer
        value
        """

        if reg.is_writeable():
            size_type = self._register_size_type(reg)

            gadget = self.gadgets["shoulder.c.function_definition"]
            gadget.return_type = size_type
            gadget.args = [(size_type, "val")]
            gadget.name = "{prefix}_{rname}_{fname}_{suffix}".format(
                prefix=self._register_function_prefix(reg),
                rname=reg.name.lower(),
                fname=field.name.lower(),
                suffix=config.bit_clear_function + "_val"
            )

            self._bitfield_clear_val(outfile, reg, field)

    @shoulder.gadget.c.function_definition
    def _bitfield_clear_val(self, outfile, reg, field):
        f_body = "return val & ~{mask};".format(
            mask=self._field_mask_string(reg, field)
        )
        outfile.write(f_body)

# ----------------------------------------------------------------------------
# bitfield_is_disabled
# ----------------------------------------------------------------------------
    def _generate_bitfield_is_clear(self, outfile, reg, field):
        """
        Generate a C function that checks if the given bitfield is disabled (0)
        in the given register
        """

        if reg.is_readable():
            size_type = self._register_size_type(reg)

            gadget = self.gadgets["shoulder.c.function_definition"]
            gadget.return_type = size_type
            gadget.args = []
            gadget.name = "{prefix}_{rname}_{fname}_{suffix}".format(
                prefix=self._register_function_prefix(reg),
                rname=reg.name.lower(),
                fname=field.name.lower(),
                suffix=config.is_bit_cleared_function
            )

            self._bitfield_is_clear(outfile, reg, field)

    @shoulder.gadget.c.function_definition
    def _bitfield_is_clear(self, outfile, reg, field):
        f_body = "{size} val = {reg_get}();\n"
        f_body += "return (val & {mask}) == 0;"

        f_body = f_body.format(
            size=self._register_size_type(reg),
            mask=self._field_mask_string(reg, field),
            reg_get=self._register_read_function_name(reg),
        )

        outfile.write(f_body)

# ----------------------------------------------------------------------------
# bitfield_is_disabled_val
# ----------------------------------------------------------------------------
    def _generate_bitfield_is_clear_val(self, outfile, reg, field):
        """
        Generate a C function that checks if the given bitfield is cleared (0)
        in an integer value
        """

        if reg.is_readable():
            size_type = self._register_size_type(reg)

            gadget = self.gadgets["shoulder.c.function_definition"]
            gadget.return_type = size_type
            gadget.args = [(size_type, "val")]
            gadget.name = "{prefix}_{rname}_{fname}_{suffix}".format(
                prefix=self._register_function_prefix(reg),
                rname=reg.name.lower(),
                fname=field.name.lower(),
                suffix=config.is_bit_cleared_function + "_val"
            )

            self._bitfield_is_clear_val(outfile, reg, field)

    @shoulder.gadget.c.function_definition
    def _bitfield_is_clear_val(self, outfile, reg, field):
        f_body = "return (val & {mask}) == 0;"

        f_body = f_body.format(
            size=self._register_size_type(reg),
            mask=self._field_mask_string(reg, field),
            reg_get=self._register_read_function_name(reg),
        )

        outfile.write(f_body)

# ----------------------------------------------------------------------------
# field_get
# ----------------------------------------------------------------------------
    def _generate_field_get(self, outfile, reg, field):
        """
        Generate a C function that reads the given field from the given register
        """

        if reg.is_readable():
            size_type = self._register_size_type(reg)

            gadget = self.gadgets["shoulder.c.function_definition"]
            gadget.return_type = size_type
            gadget.args = []
            gadget.name = "{prefix}_{rname}_{fname}_{suffix}".format(
                prefix=self._register_function_prefix(reg),
                rname=reg.name.lower(),
                fname=field.name.lower(),
                suffix=config.register_field_read_function
            )

            self._field_get(outfile, reg, field)

    @shoulder.gadget.c.function_definition
    def _field_get(self, outfile, reg, field):
        f_body = "{size} val = {reg_get}();\n"
        f_body += "return (val & {mask}) >> {lsb};"

        f_body = f_body.format(
            size=self._register_size_type(reg),
            mask=self._field_mask_string(reg, field),
            lsb=self._field_lsb_string(reg, field),
            reg_get=self._register_read_function_name(reg)
        )

        outfile.write(f_body)

# ----------------------------------------------------------------------------
# field_get_val
# ----------------------------------------------------------------------------
    def _generate_field_get_val(self, outfile, reg, field):
        """
        Generate a C function that reads the given field from an integer value
        """

        if reg.is_readable():
            size_type = self._register_size_type(reg)

            gadget = self.gadgets["shoulder.c.function_definition"]
            gadget.return_type = size_type
            gadget.args = [(size_type, "val")]
            gadget.name = "{prefix}_{rname}_{fname}_{suffix}".format(
                prefix=self._register_function_prefix(reg),
                rname=reg.name.lower(),
                fname=field.name.lower(),
                suffix=config.register_field_read_function + "_val"
            )

            self._field_get_val(outfile, reg, field)

    @shoulder.gadget.c.function_definition
    def _field_get_val(self, outfile, reg, field):
        f_body = "return (val & {mask}) >> {lsb};"

        f_body = f_body.format(
            size=self._register_size_type(reg),
            mask=self._field_mask_string(reg, field),
            lsb=self._field_lsb_string(reg, field)
        )

        outfile.write(f_body)

# ----------------------------------------------------------------------------
# field_set
# ----------------------------------------------------------------------------
    def _generate_field_set(self, outfile, reg, field):
        """
        Generate a C function that writes the given field to the given register
        """

        if reg.is_writeable() and reg.is_readable():
            size_type = self._register_size_type(reg)

            gadget = self.gadgets["shoulder.c.function_definition"]
            gadget.return_type = size_type
            gadget.args = [(size_type, "val")]
            gadget.name = "{prefix}_{rname}_{fname}_{suffix}".format(
                prefix=self._register_function_prefix(reg),
                rname=reg.name.lower(),
                fname=field.name.lower(),
                suffix=config.register_field_write_function
            )

            self._field_set(outfile, reg, field)

    @shoulder.gadget.c.function_definition
    def _field_set(self, outfile, reg, field):
        f_body = "{size} reg = ({reg_get}() & ~{mask})\n"
        f_body += "\t| ((val << {lsb}) & {mask});\n"
        f_body += "{reg_set}(reg);"

        f_body = f_body.format(
            size=self._register_size_type(reg),
            mask=self._field_mask_string(reg, field),
            lsb=self._field_lsb_string(reg, field),
            reg_get=self._register_read_function_name(reg),
            reg_set=self._register_write_function_name(reg)
        )

        outfile.write(f_body)

# ----------------------------------------------------------------------------
# field_set_val
# ----------------------------------------------------------------------------
    def _generate_field_set_val(self, outfile, reg, field):
        """
        Generate a C function that writes the given field to an integer value
        """

        if reg.is_writeable():
            size_type = self._register_size_type(reg)

            gadget = self.gadgets["shoulder.c.function_definition"]
            gadget.return_type = size_type
            gadget.args = [(size_type, "field_val"), (size_type, "reg_val")]
            gadget.name = "{prefix}_{rname}_{fname}_{suffix}".format(
                prefix=self._register_function_prefix(reg),
                rname=reg.name.lower(),
                fname=field.name.lower(),
                suffix=config.register_field_write_function + "_val"
            )

            self._field_set_val(outfile, reg, field)

    @shoulder.gadget.c.function_definition
    def _field_set_val(self, outfile, reg, field):
        f_body = "return (reg_val & ~{mask})\n\t"
        f_body += "| ((field_val << {lsb}) & {mask});"

        f_body = f_body.format(
            size=self._register_size_type(reg),
            mask=self._field_mask_string(reg, field),
            lsb=self._field_lsb_string(reg, field)
        )

        outfile.write(f_body)

# ----------------------------------------------------------------------------
# utilities
# ----------------------------------------------------------------------------
    def _register_function_prefix(self, reg):
        p = config.c_prefix
        if reg.execution_state:
            return p + str(reg.execution_state)
        elif not reg.is_internal:
            return p + "external"
        else:
            return p

    def _field_mask_hex_string(self, reg, field):
        mask_val = 0
        for i in range(field.lsb, field.msb + 1):
            mask_val |= 1 << i

        if reg.size == 32:
            return "{0:#0{1}x}".format(mask_val, 10)
        else:
            return "{0:#0{1}x}".format(mask_val, 18)

    def _field_mask_string(self, reg, field):
        return "{prefix}_{reg}_{field}_mask".format(
            prefix=self._register_function_prefix(reg),
            reg=reg.name.lower(),
            field=field.name.lower()
        )

    def _field_lsb_string(self, reg, field):
        return "{prefix}_{reg}_{field}_lsb".format(
            prefix=self._register_function_prefix(reg),
            reg=reg.name.lower(),
            field=field.name.lower()
        )

    def _register_size_type(self, reg):
        if reg.size == 32:
            return "uint32_t"
        else:
            return "uint64_t"

    def _register_read_function_name(self, reg):
        return "{prefix}_{reg_name}_{read}".format(
            prefix=self._register_function_prefix(reg),
            reg_name=reg.name.lower(),
            read=config.register_read_function
        )

    def _register_write_function_name(self, reg):
        return "{prefix}_{reg_name}_{write}".format(
            prefix=self._register_function_prefix(reg),
            reg_name=reg.name.lower(),
            write=config.register_write_function
        )
