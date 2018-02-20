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
from shoulder.register import Register
from shoulder.fieldset import Fieldset
from shoulder.logger import logger
from shoulder.exception import *


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
                logger.debug("Register Attributes:")
                reg = Register()
                self._set_register_name(reg, reg_node)
                self._set_register_long_name(reg, reg_node)
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

    def _set_register_purpose(self, reg, reg_node):
        purpose_text_nodes = reg_node.findall("./reg_purpose/purpose_text")
        if len(purpose_text_nodes) == 1:
            purpose_node = reg_node.find("./reg_purpose/purpose_text/para")
            if purpose_node is not None:
                ET.strip_tags(purpose_node, "arm-defined-word", "register_link")
                reg.purpose = purpose_node.text
        elif len(purpose_text_nodes) > 1:
            text = "See the ARMv" + str(self.aarch_version_major)
            if self.aarch_version_minor is not None:
                text += "." + str(self.aarch_version_minor)
            text += " architecture reference manual for a description"
            text += " of this register"
            reg.purpose = text

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
            logger.warn(str(reg.name) + " size attribute not found")

    def _set_register_fields(self, reg, reg_node):
        fields_node_list = reg_node.findall("./reg_fieldsets/fields")

        for fields_node in fields_node_list:
            fieldset = Fieldset(int(reg.size))
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
                msb = int(field_node.find("./field_msb").text)
                lsb = int(field_node.find("./field_lsb").text)
                fieldset.add_field(name, msb, lsb)
                dbg_msg += str(name) + " (" + str(msb) + ":" + str(lsb) + ") "

            reg.add_fieldset(fieldset)
            logger.debug(dbg_msg)
