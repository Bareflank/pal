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

from lxml import etree as ET

from shoulder.parser.abstract_parser import AbstractParser
from shoulder.logger import logger
from shoulder.exception import *
import shoulder.model as model

class ArmV8XmlParser(AbstractParser):
    @property
    def aarch_version_major(self):
        return 8

    @property
    def aarch_version_minor(self):
        return None

    def parse_registers(self, path):
        registers = []

        try:
            etree = ET.parse(path)
            root_node = etree.getroot()
            registers_node = root_node.findall("./registers/register")
            reg_count = len(registers_node)
            msg = type(self).__name__ + ": processing " + str(reg_count)
            msg += " register " if reg_count == 1 else " registers "
            msg += "from " + str(path)
            logger.debug(msg)

            for reg_node in registers_node:
                if (str(reg_node.attrib["is_register"]) == "True"):
                    logger.debug("Register Attributes:")
                    reg = model.Register()
                    self._set_register_name(reg, reg_node)
                    self._set_register_long_name(reg, reg_node)
                    self._set_register_access_attributes(reg, reg_node)
                    self._set_register_access_mechanisms(reg, reg_node)
                    self._set_register_purpose(reg, reg_node)
                    self._set_register_size(reg, reg_node)
                    self._set_register_fields(reg, reg_node)
                    registers.append(reg)

        except Exception as e:
            msg = "Failed to parse register file " + str(path)
            msg += ": " + str(e)
            raise ShoulderParserException(msg)

        return registers

    def parse_instructions(self, path):
        raise NotImplementedError(type(self).__name__ + ".parse_instructions not yet implemented")

    def _set_register_name(self, reg, reg_node):
        name_node = reg_node.find("./reg_short_name")
        if name_node is not None:
            reg.name = name_node.text
            logger.debug("name = " + reg.name)
        else:
            logger.error("register name not found")
            raise ShoulderParserException()

    def _set_register_long_name(self, reg, reg_node):
        long_name_node = reg_node.find("./reg_long_name")
        if long_name_node is not None:
            reg.long_name = long_name_node.text
            logger.debug("long_name = " + reg.long_name)
        else:
            logger.warn(str(reg.name) + " long_name attribute not found")

    def _set_register_access_attributes(self, reg, reg_node):
        access_mechanism_nodes = reg_node.findall("./access_mechanisms/access_mechanism")
        for mechanism in access_mechanism_nodes:
            if mechanism is not None:
                accessor = str(mechanism.attrib["accessor"])
                operation = accessor.split(' ', 1)[0]
                if operation == "MSR" or operation == "MSRregister":
                    reg.is_writable = True
                if reg.access_attributes is None:
                    access_attributes = model.AccessAttributes()
                    if operation.startswith("MR"):
                        access_attributes.mnemonic = accessor.split(' ', 1)[1]

                    encoding_nodes = mechanism.findall("encoding/enc")
                    for enc in encoding_nodes:
                        name = str(enc.attrib["n"])
                        try:
                            val = int(enc.attrib["v"], 2)
                        except:
                            continue

                        if name == "op0":
                            access_attributes.op0 = val
                        elif name == "op1":
                            access_attributes.op1 = val
                        elif name == "op2":
                            access_attributes.op2 = val
                        elif name == "CRn":
                            access_attributes.crn = val
                        elif name == "CRm":
                            access_attributes.crm = val

                    if access_attributes.is_valid():
                        reg.access_attributes = access_attributes
            else:
                logger.warn(str(reg.name) + " access_mechanism attribute not found")

    def _set_register_access_mechanisms(self, reg, reg_node):
        # Memory mapped access mechanisms
        reg_address_nodes = reg_node.findall("./reg_address")
        offsets = set()
        for node in reg_address_nodes:
            offset_node = node.find("./reg_offset/hexnumber")
            offset = int(offset_node.text, 0)
            offsets.add(offset)

            access_type_nodes = node.findall("./reg_access/reg_access_state/reg_access_type")
            access_types = set()
            for access_type_node in access_type_nodes:
                access_type = access_type_node.text
                access_types.add(access_type)

            readable_types = set(["RO", "RW", "WI", "IMPDEF", "RO or RW", "RAZ/WI"])
            writable_types = set(["RW", "WO", "RO or RW", "IMPDEF"])

            if access_types & readable_types:
                am = model.access_mechanism.ReadMemoryMapped(offset)
                reg.access_mechanisms.append(am)

            if access_types & writable_types:
                am = model.access_mechanism.WriteMemoryMapped(offset)
                reg.access_mechanisms.append(am)

        # Instruction based access mechanisms
        access_mechanism_nodes = reg_node.findall("./access_mechanisms/access_mechanism")
        for access_mechanism_node in access_mechanism_nodes:
            try:
                accessor = str(access_mechanism_node.attrib["accessor"])
                operation = accessor.split(' ', 1)[0]
                operand = accessor.split(' ', 1)[1]

                encoding_nodes = access_mechanism_node.findall("encoding/enc")
                encoding = {}
                for enc in encoding_nodes:
                    name = str(enc.attrib["n"]).lower()
                    val = int(enc.attrib["v"], 2)
                    encoding[name] = val

                if operation == "MSRregister":
                    am = model.access_mechanism.WriteSystemRegister(
                        encoding["op0"], encoding["op1"], encoding["op2"],
                        encoding["crn"], encoding["crm"], operand, rt=0b0
                    )
                    reg.access_mechanisms.append(am)

                elif operation == "MSRbanked":
                    am = model.access_mechanism.WriteSystemRegisterBanked(
                        encoding["m"], encoding["r"], encoding["m1"], operand
                    )
                    reg.access_mechanisms.append(am)

                elif operation == "MSRimmediate":
                    am = model.access_mechanism.WriteSystemRegisterImmediate(
                        encoding["crn"], encoding["op0"],
                        encoding["op1"], encoding["op2"], operand
                    )
                    reg.access_mechanisms.append(am)

                elif operation == "MRS":
                    am = model.access_mechanism.ReadSystemRegister(
                        encoding["op0"], encoding["op1"], encoding["op2"],
                        encoding["crn"], encoding["crm"], operand, rt=0b0
                    )
                    reg.access_mechanisms.append(am)

                elif operation == "MRSbanked":
                    am = model.access_mechanism.ReadSystemRegisterBanked(
                        encoding["m"], encoding["r"], encoding["m1"], operand
                    )
                    reg.access_mechanisms.append(am)

                elif operation == "MCR":
                    am = model.access_mechanism.WriteCoprocessorRegister(
                        encoding["coproc"], encoding["opc1"], encoding["opc2"],
                        encoding["crn"], encoding["crm"], operand
                    )
                    reg.access_mechanisms.append(am)

                elif operation == "MCRR":
                    am = model.access_mechanism.WriteCoprocessorRegister2(
                        encoding["coproc"], encoding["opc1"], encoding["crm"],
                        operand
                    )
                    reg.access_mechanisms.append(am)

                elif operation == "MRC":
                    am = model.access_mechanism.ReadCoprocessorRegister(
                        encoding["coproc"], encoding["opc1"], encoding["opc2"],
                        encoding["crn"], encoding["crm"], operand
                    )
                    reg.access_mechanisms.append(am)

                elif operation == "MRRC":
                    am = model.access_mechanism.ReadCoprocessorRegister2(
                        encoding["coproc"], encoding["opc1"], encoding["crm"],
                        operand
                    )
                    reg.access_mechanisms.append(am)

                elif operation == "VMRS":
                    am = model.access_mechanism.ReadSystemVectorRegister(
                        encoding["reg"], operand
                    )
                    reg.access_mechanisms.append(am)

                elif operation == "VMSR":
                    am = model.access_mechanism.WriteSystemVectorRegister(
                        encoding["reg"], operand
                    )
                    reg.access_mechanisms.append(am)

                else:
                    msg = "Invalid operation " + operation
                    msg += " in register " + reg.name
                    raise ShoulderParserException(msg)

                logger.debug(str(am))

            except Exception as e:
                msg = "Could not parse " + str(operation) + " access mechanism"
                msg += " in register " + reg.name + ":"
                logger.warn(msg)
                logger.warn("\t" + str(e))
                continue


    def _set_register_purpose(self, reg, reg_node):
        purpose_text_nodes = reg_node.findall("./reg_purpose/purpose_text")
        if len(purpose_text_nodes) == 1:
            purpose_node = reg_node.find("./reg_purpose/purpose_text/para")
            if purpose_node is not None:
                ET.strip_tags(purpose_node, "arm-defined-word", "register_link")
                reg.purpose = purpose_node.text
                reg.purpose = reg.purpose.replace("\n", " ")
        elif len(purpose_text_nodes) > 1:
            text = "See the ARMv" + str(self.aarch_version_major)
            if self.aarch_version_minor is not None:
                text += "." + str(self.aarch_version_minor)
            text += " architecture reference manual for a description"
            text += " of this register"
            reg.purpose = text
            reg.purpose = reg.purpose.replace("\n", " ")

        if reg.purpose is not None:
            logger.debug("purpose = " + reg.purpose)
        else:
            logger.warn(str(reg.name) + " purpose attribute not found")


    def _set_register_size(self, reg, reg_node):
        fields_node = reg_node.find("./reg_fieldsets/fields")

        if fields_node is not None:
            reg.size = int(fields_node.attrib["length"])
            logger.debug("size = " + str(reg.size))
        else:
            reg.size = None
            logger.debug(str(reg.name) + " size attribute not found")

    def _set_register_fields(self, reg, reg_node):
        fields_node_list = reg_node.findall("./reg_fieldsets/fields")

        for fields_node in fields_node_list:
            fieldset = model.Fieldset(int(reg.size))
            fieldset_condition_node = fields_node.find("./fields_condition")
            field_node_list = fields_node.findall("./field")
            dbg_msg = "fieldset: "

            if fieldset_condition_node is not None:
                fieldset.condition = fieldset_condition_node.text

            for field_node in field_node_list:
                name_node = field_node.find("./field_name")
                if name_node is None:
                    name_node = field_node.find("./field_shortdesc")
                if name_node is None:
                    error_msg = str(reg.name) + " invalid field"
                    logger.error(error_msg)
                    raise ShoulderParserException(error_msg)

                name = name_node.text
                name = name.replace(" ", "_")
                msb = int(field_node.find("./field_msb").text)
                lsb = int(field_node.find("./field_lsb").text)
                fieldset.add_field(name, msb, lsb)
                dbg_msg += str(name) + " (" + str(msb) + ":" + str(lsb) + ") "

            reg.add_fieldset(fieldset)
            logger.debug(dbg_msg)
