import re
from lxml import etree as ET

from pal.parser.abstract_parser import AbstractParser
from pal.logger import logger
from pal.exception import PalParserException
import pal.model
import pal.model.armv8a
import pal.model.armv8a.access_mechanism


class ArmV8XmlParser(AbstractParser):
    def parse_file(self, path):
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

                    reg = pal.model.armv8a.ARMv8ARegister()
                    self._set_register_name(reg, reg_node)

                    if "<n>" in reg.name:
                        array_start_node = reg_node.find("./reg_array/reg_array_start")
                        array_end_node = reg_node.find("./reg_array/reg_array_end")

                        if array_start_node is None or array_end_node is None:
                            logger.warn("Unbounded n-index register " + str(reg.name))
                            continue

                        array_start = int(array_start_node.text)
                        array_end = int(array_end_node.text)

                        # TODO: Figure out better way to identify long
                        # memory-mapped registers and access them with an
                        # offset
                        if ((array_end - array_start) > 32):
                            logger.warn("Excessively large n-index register " + str(reg.name))
                            continue

                        for n in range(array_start, array_end + 1):
                            n_reg = pal.model.armv8a.ARMv8ARegister()
                            self._set_register_name(n_reg, reg_node)
                            self._set_register_long_name(n_reg, reg_node)
                            self._set_register_execution_state(n_reg, reg_node)
                            self._set_register_attributes(n_reg, reg_node)
                            self._set_register_access_mechanisms(n_reg, reg_node, n)
                            self._set_register_purpose(n_reg, reg_node)
                            self._set_register_size(n_reg, reg_node)
                            self._set_register_fields(n_reg, reg_node)

                            n_reg.name = n_reg.name.replace("<n>", str(n))
                            for fs in n_reg.fieldsets:
                                for f in fs.fields:
                                    f.name = f.name.replace("<n>", str(n))

                            registers.append(n_reg)
                    else:
                        self._set_register_long_name(reg, reg_node)
                        self._set_register_execution_state(reg, reg_node)
                        self._set_register_attributes(reg, reg_node)
                        self._set_register_access_mechanisms(reg, reg_node)
                        self._set_register_purpose(reg, reg_node)
                        self._set_register_size(reg, reg_node)
                        self._set_register_fields(reg, reg_node)
                        registers.append(reg)

        except Exception as e:
            msg = "Failed to parse register file " + str(path)
            msg += ": " + str(e)
            raise PalParserException(msg)

        return registers

    def _set_register_name(self, reg, reg_node):
        name_node = reg_node.find("./reg_short_name")
        if name_node is not None:
            reg.name = name_node.text
            logger.debug("name = " + reg.name)
        else:
            logger.error("register name not found")
            raise PalParserException()

    def _set_register_long_name(self, reg, reg_node):
        long_name_node = reg_node.find("./reg_long_name")
        if long_name_node is not None:
            reg.long_name = long_name_node.text
            logger.debug("long_name = " + reg.long_name)
        else:
            logger.warn(str(reg.name) + " long_name attribute not found")

    def _set_register_execution_state(self, reg, reg_node):
        if "execution_state" in reg_node.attrib:
            reg.execution_state = reg_node.attrib["execution_state"].lower()
        else:
            reg.execution_state = None

    def _set_register_attributes(self, reg, reg_node):
        if "is_internal" in reg_node.attrib:
            val = reg_node.attrib["is_internal"]
            reg.is_internal = True if val == "True" else False

        if "is_banked" in reg_node.attrib:
            val = reg_node.attrib["is_banked"]
            reg.is_banked = True if val == "True" else False

        if "is_optional" in reg_node.attrib:
            val = reg_node.attrib["is_optional"]
            reg.is_optional = True if val == "True" else False

    def _set_register_access_mechanisms(self, reg, reg_node, n=0):
        # Memory mapped access mechanisms
        reg_address_nodes = reg_node.findall("./reg_address")
        offsets = set()
        for node in reg_address_nodes:
            component_node = node.find("./reg_component")
            component = str(component_node.text).lower()
            component = component.replace(" ", "_")
            component = component.replace(".", "_")

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
                am = pal.model.armv8a.access_mechanism.LDR(component, offset)
                reg.access_mechanisms["ldr"].append(am)

            if access_types & writable_types:
                am = pal.model.armv8a.access_mechanism.STR(component, offset)
                reg.access_mechanisms["str"].append(am)

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
                    try:
                        val = int(enc.attrib["v"], 2)
                    except ValueError:
                        strval = str(enc.attrib["v"])
                        n_field_strings = re.findall("\[n:\d+:\d+]", strval)
                        for n_string in n_field_strings:
                            n_trim = n_string[1:-1]
                            msb = int(n_trim.split(":")[1])
                            lsb = int(n_trim.split(":")[2])
                            replacement = ""
                            for i in range(lsb, msb + 1):
                                if ((1 << i) & n):
                                    replacement = "1" + replacement
                                else:
                                    replacement = "0" + replacement
                            strval = strval.replace(n_string, replacement)

                        n_bit_strings = re.findall("\[n:\d+]", strval)
                        for n_string in n_bit_strings:
                            n_trim = n_string[1:-1]
                            bit = int(n_trim.split(":")[1])
                            n_bit = bin(((1 << bit) & n) >> bit)
                            strval = strval.replace(n_string, str(n_bit)[2:])

                        n_strings = re.findall("n+", strval)
                        for n_string in n_strings:
                            num_bits = len(n_string)
                            replacement = ""
                            for i in range(num_bits):
                                if ((1 << i) & n):
                                    replacement = "1" + replacement
                                else:
                                    replacement = "0" + replacement
                            strval = strval.replace(n_string, replacement)

                        val = int(strval, 2)
                        operand = operand.replace("<n>", str(n))
                    encoding[name] = val

                if operation == "MSRregister":
                    am = pal.model.armv8a.access_mechanism.MSRRegister(
                        encoding["op0"], encoding["op1"], encoding["op2"],
                        encoding["crn"], encoding["crm"], operand, rt=0b0
                    )
                    reg.access_mechanisms["msr_register"].append(am)

                elif operation == "MSRbanked":
                    am = pal.model.armv8a.access_mechanism.MSRBanked(
                        encoding["m"], encoding["r"], encoding["m1"], operand
                    )
                    reg.access_mechanisms["msr_banked"].append(am)

                elif operation == "MSRimmediate":
                    am = pal.model.armv8a.access_mechanism.MSRImmediate(
                        encoding["crn"], encoding["op0"],
                        encoding["op1"], encoding["op2"], operand
                    )
                    reg.access_mechanisms["msr_immediate"].append(am)

                elif operation == "MRS":
                    am = pal.model.armv8a.access_mechanism.MRSRegister(
                        encoding["op0"], encoding["op1"], encoding["op2"],
                        encoding["crn"], encoding["crm"], operand, rt=0b0
                    )
                    reg.access_mechanisms["mrs_register"].append(am)

                elif operation == "MRSbanked":
                    am = pal.model.armv8a.access_mechanism.MRSBanked(
                        encoding["m"], encoding["r"], encoding["m1"], operand
                    )
                    reg.access_mechanisms["mrs_banked"].append(am)

                elif operation == "MCR":
                    am = pal.model.armv8a.access_mechanism.MCR(
                        encoding["coproc"], encoding["opc1"], encoding["opc2"],
                        encoding["crn"], encoding["crm"]
                    )
                    reg.access_mechanisms["mcr"].append(am)

                elif operation == "MCRR":
                    am = pal.model.armv8a.access_mechanism.MCRR(
                        encoding["coproc"], encoding["opc1"], encoding["crm"]
                    )
                    reg.access_mechanisms["mcrr"].append(am)

                elif operation == "MRC":
                    am = pal.model.armv8a.access_mechanism.MRC(
                        encoding["coproc"], encoding["opc1"], encoding["opc2"],
                        encoding["crn"], encoding["crm"]
                    )
                    reg.access_mechanisms["mrc"].append(am)

                elif operation == "MRRC":
                    am = pal.model.armv8a.access_mechanism.MRRC(
                        encoding["coproc"], encoding["opc1"], encoding["crm"]
                    )
                    reg.access_mechanisms["mrrc"].append(am)

                elif operation == "VMRS":
                    am = pal.model.armv8a.access_mechanism.VMRS(
                        encoding["reg"], operand
                    )
                    reg.access_mechanisms["vmrs"].append(am)

                elif operation == "VMSR":
                    am = pal.model.armv8a.access_mechanism.VMSR(
                        encoding["reg"], operand
                    )
                    reg.access_mechanisms["vmsr"].append(am)

                else:
                    msg = "Invalid operation " + operation
                    msg += " in register " + reg.name
                    raise PalParserException(msg)

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
            text = "See the ARMv8 architecture reference manual for a "
            text += "description of this register"
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
            fieldset = pal.model.Fieldset(int(reg.size))
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
                    raise PalParserException(error_msg)

                name = name_node.text
                name = name.replace(" ", "_")
                msb = int(field_node.find("./field_msb").text)
                lsb = int(field_node.find("./field_lsb").text)
                fieldset.add_field(name, msb, lsb)
                dbg_msg += str(name) + " (" + str(msb) + ":" + str(lsb) + ") "

            reg.fieldsets.append(fieldset)
            logger.debug(dbg_msg)
