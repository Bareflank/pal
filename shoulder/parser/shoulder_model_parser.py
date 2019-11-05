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

from shoulder.parser.abstract_parser import AbstractParser
from shoulder.logger import logger
from shoulder.exception import ShoulderParserException
import shoulder.model
import shoulder.model.armv8a
import shoulder.model.armv8a.access_mechanism
import shoulder.model.x86_64
import shoulder.model.x86_64.access_mechanism

from yaml import load, dump
from yaml import CLoader as Loader, CDumper as Dumper


class ShoulderModelParser(AbstractParser):
    def parse_file(self, path):
        registers = []

        try:
            if "__template__" in path:
                return []

            with open(path, "r") as infile:
                data = load(infile, Loader)

                for item in data:
                    arch = item["arch"]

                    if arch == "x86_64":
                        register = shoulder.model.x86_64.register.x86_64Register()
                    elif arch == "armv8-a":
                        register = shoulder.model.armv8a.register.ARMv8ARegister()
                    else:
                        raise Exception("register definition missing architecutre (arch)")

                    self._parse_register(register, item)
                    self._parse_access_mechanisms(register, item)
                    self._parse_fieldsets(register, item)

                    registers.append(register)

        except Exception as e:
            msg = "Failed to parse register file " + str(path)
            msg += ": " + str(e)
            raise ShoulderParserException(msg)

        return registers

    def _parse_register(self, register, yml):
        register.name = self._strip_string(yml["name"])
        register.size = yml["size"]
        if "long_name" in yml:
            register.long_name = self._strip_string(yml["long_name"])
        if "purpose" in yml:
            register.purpose = self._strip_string(yml["purpose"])
        if "arch" in yml:
            register.arch = self._strip_string(yml["arch"])
        if "is_internal" in yml:
            register.is_internal = yml["is_internal"]
        if "is_optional" in yml:
            register.is_optional = yml["is_optional"]
        if "is_indexed" in yml:
            register.is_indexed = yml["is_indexed"]
        if "execution_state" in yml:
            register.execution_state = yml["execution_state"]
        if "is_banked" in yml:
            register.is_banked = yml["is_banked"]

    def _parse_access_mechanisms(self, register, yml):
        if not yml["access_mechanisms"]:
            return

        for am_yml in yml["access_mechanisms"]:
            if am_yml["name"] == "mov_read":
                am = shoulder.model.x86_64.access_mechanism.MOVRead()
                am.name = am_yml["name"]
                am.source_mnemonic = am_yml["source_mnemonic"]
                register.access_mechanisms["mov_read"].append(am)

            elif am_yml["name"] == "mov_write":
                am = shoulder.model.x86_64.access_mechanism.MOVWrite()
                am.name = am_yml["name"]
                am.destination_mnemonic = am_yml["destination_mnemonic"]
                register.access_mechanisms["mov_write"].append(am)

            elif am_yml["name"] == "cpuid":
                am = shoulder.model.x86_64.access_mechanism.CPUID()
                am.name = am_yml["name"]
                am.leaf = am_yml["leaf"]
                am.output = am_yml["output"]
                register.access_mechanisms["cpuid"].append(am)

            elif am_yml["name"] == "rdmsr":
                am = shoulder.model.x86_64.access_mechanism.RDMSR()
                am.name = am_yml["name"]
                am.address = am_yml["address"]
                register.access_mechanisms["rdmsr"].append(am)

            elif am_yml["name"] == "wrmsr":
                am = shoulder.model.x86_64.access_mechanism.WRMSR()
                am.name = am_yml["name"]
                am.address = am_yml["address"]
                register.access_mechanisms["wrmsr"].append(am)

            elif am_yml["name"] == "mrs_register":
                am = shoulder.model.armv8a.access_mechanism.MRSRegister()
                am.name = am_yml["name"]
                am.op0 = am_yml["op0"]
                am.op1 = am_yml["op1"]
                am.op2 = am_yml["op2"]
                am.crn = am_yml["crn"]
                am.crm = am_yml["crm"]
                am.operand_mnemonic = am_yml["operand_mnemonic"]
                register.access_mechanisms["mrs_register"].append(am)

            elif am_yml["name"] == "msr_register":
                am = shoulder.model.armv8a.access_mechanism.MSRRegister()
                am.name = am_yml["name"]
                am.op0 = am_yml["op0"]
                am.op1 = am_yml["op1"]
                am.op2 = am_yml["op2"]
                am.crn = am_yml["crn"]
                am.crm = am_yml["crm"]
                am.operand_mnemonic = am_yml["operand_mnemonic"]
                register.access_mechanisms["msr_register"].append(am)

            elif am_yml["name"] == "mcr":
                am = shoulder.model.armv8a.access_mechanism.MCR()
                am.name = am_yml["name"]
                am.coproc = am_yml["coproc"]
                am.opc1 = am_yml["opc1"]
                am.opc2 = am_yml["opc2"]
                am.crn = am_yml["crn"]
                am.crm = am_yml["crm"]
                register.access_mechanisms["mcr"].append(am)

            elif am_yml["name"] == "mcrr":
                am = shoulder.model.armv8a.access_mechanism.MCRR()
                am.name = am_yml["name"]
                am.coproc = am_yml["coproc"]
                am.opc1 = am_yml["opc1"]
                am.crm = am_yml["crm"]
                register.access_mechanisms["mcrr"].append(am)

            elif am_yml["name"] == "mrc":
                am = shoulder.model.armv8a.access_mechanism.MRC()
                am.name = am_yml["name"]
                am.coproc = am_yml["coproc"]
                am.opc1 = am_yml["opc1"]
                am.opc2 = am_yml["opc2"]
                am.crn = am_yml["crn"]
                am.crm = am_yml["crm"]
                register.access_mechanisms["mrc"].append(am)

            elif am_yml["name"] == "mrrc":
                am = shoulder.model.armv8a.access_mechanism.MRRC()
                am.name = am_yml["name"]
                am.coproc = am_yml["coproc"]
                am.opc1 = am_yml["opc1"]
                am.crm = am_yml["crm"]
                register.access_mechanisms["mrrc"].append(am)

            elif am_yml["name"] == "mrs_banked":
                am = shoulder.model.armv8a.access_mechanism.MRSBanked()
                am.name = am_yml["name"]
                am.m = am_yml["m"]
                am.r = am_yml["r"]
                am.m1 = am_yml["m1"]
                register.access_mechanisms["mrs_banked"].append(am)

            elif am_yml["name"] == "msr_banked":
                am = shoulder.model.armv8a.access_mechanism.MSRBanked()
                am.name = am_yml["name"]
                am.m = am_yml["m"]
                am.r = am_yml["r"]
                am.m1 = am_yml["m1"]
                register.access_mechanisms["msr_banked"].append(am)

            elif am_yml["name"] == "msr_immediate":
                am = shoulder.model.armv8a.access_mechanism.MSRImmediate()
                am.name = am_yml["name"]
                register.access_mechanisms["msr_immediate"].append(am)

            elif am_yml["name"] == "ldr":
                am = shoulder.model.armv8a.access_mechanism.LDR()
                am.name = am_yml["name"]
                am.component = am_yml["component"]
                am.offset = am_yml["offset"]
                register.access_mechanisms["ldr"].append(am)

            elif am_yml["name"] == "str":
                am = shoulder.model.armv8a.access_mechanism.STR()
                am.name = am_yml["name"]
                am.component = am_yml["component"]
                am.offset = am_yml["offset"]
                register.access_mechanisms["str"].append(am)

            elif am_yml["name"] == "vmrs":
                am = shoulder.model.armv8a.access_mechanism.VMRS()
                am.name = am_yml["name"]
                am.reg = am_yml["reg"]
                am.operand_mnemonic = am_yml["operand_mnemonic"]
                register.access_mechanisms["vmrs"].append(am)

            elif am_yml["name"] == "vmsr":
                am = shoulder.model.armv8a.access_mechanism.VMSR()
                am.name = am_yml["name"]
                am.reg = am_yml["reg"]
                am.operand_mnemonic = am_yml["operand_mnemonic"]
                register.access_mechanisms["vmsr"].append(am)

    def _parse_fieldsets(self, register, yml):
        if "fieldsets" not in yml:
            return

        for fieldset_yml in yml["fieldsets"]:
            fs = shoulder.model.Fieldset()
            fs.size = fieldset_yml["size"]
            if "name" in fieldset_yml:
                fs.name = fieldset_yml["name"]
            if "condition" in fieldset_yml:
                fs.condition = fieldset_yml["condition"]

            for field_yml in fieldset_yml["fields"]:
                field = shoulder.model.Field()
                field.name = self._strip_string(str(field_yml["name"]))
                field.lsb = int(field_yml["lsb"])
                field.msb = int(field_yml["msb"])
                if "long_name" in field_yml:
                    field.long_name = self._strip_string(field_yml["long_name"])
                if "description" in field_yml:
                    field.description = self._strip_string(field_yml["description"])
                if "readable" in field_yml:
                    field.readable = field_yml["readable"]
                if "writable" in field_yml:
                    field.writable = field_yml["writable"]
                if "lockable" in field_yml:
                    field.lockable = field_yml["lockable"]
                if "write_once" in field_yml:
                    field.write_once = field_yml["write_once"]
                if "write_1_clear" in field_yml:
                    field.write_1_clear = field_yml["write_1_clear"]
                if "reserved0" in field_yml:
                    field.reserved0 = field_yml["reserved0"]
                if "reserved1" in field_yml:
                    field.reserved1 = field_yml["reserved1"]
                if "preserved" in field_yml:
                    field.preserved = field_yml["preserved"]

                fs.fields.append(field)

            register.fieldsets.append(fs)

    def _strip_string(self, string):
        if string.startswith("\""):
            return self._strip_string(string[1:])
        elif string.startswith("\ "):
            return self._strip_string(string[1:])
        elif string.startswith("\n"):
            return self._strip_string(string[1:])

        elif string.endswith("\n"):
            return self._strip_string(string[:-1])
        elif string.endswith("\""):
            return self._strip_string(string[:-1])
        elif string.endswith(";"):
            return self._strip_string(string[:-1])
        elif string.endswith("\ "):
            return self._strip_string(string[:-1])

        return string
