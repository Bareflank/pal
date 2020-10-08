from pal.parser.abstract_parser import AbstractParser
from pal.logger import logger
from pal.exception import PalParserException
import pal.model

from yaml import load, dump
from yaml import CLoader as Loader, CDumper as Dumper


class PalInstructionModelParser():
    def parse_instructions_from_file(self, path):
        instructions = []

        try:
            if "__template__" in path:
                return []

            with open(path, "r", encoding="utf8") as infile:
                data = load(infile, Loader)

                for item in data:
                    instruction = pal.model.instruction.Instruction()

                    self._parse_instruction(instruction, item)
                    self._parse_execution_contexts(instruction, item)

                    instructions.append(instruction)

        except Exception as e:
            msg = "Failed to parse instruction file " + str(path)
            msg += ": " + str(e)
            raise PalParserException(msg)

        return instructions

    def _parse_instruction(self, instruction, yml):
        instruction.name = self._strip_string(yml["name"])
        if "long_name" in yml:
            instruction.long_name = self._strip_string(yml["long_name"])
        if "purpose" in yml:
            instruction.purpose = self._strip_string(yml["purpose"])


    def _parse_execution_contexts(self, instruction, yml):
        if not yml["execution_contexts"]:
            return

        for ec_yml in yml["execution_contexts"]:
            ec = pal.model.execution_context.ExecutionContext()

            if "execution_state" in ec_yml:
                ec.execution_state = self._strip_string(ec_yml["execution_state"])

            if "logical_inputs" in ec_yml:
                for li_yml in ec_yml["logical_inputs"]:
                    logical_operand = pal.model.logical_operand.LogicalOperand()
                    logical_operand.name = li_yml["name"]
                    logical_operand.type = li_yml["type"]
                    ec.logical_inputs.append(logical_operand)

            if "logical_outputs" in ec_yml:
                for lo_yml in ec_yml["logical_outputs"]:
                    logical_operand = pal.model.logical_operand.LogicalOperand()
                    logical_operand.name = lo_yml["name"]
                    logical_operand.type = lo_yml["type"]
                    ec.logical_outputs.append(logical_operand)

            if "register_operands" in ec_yml:
                for reg_op_yml in ec_yml["register_operands"]:
                    register_operand = pal.model.register_operand.RegisterOperand()
                    register_operand.name = reg_op_yml["name"]
                    if "input" in reg_op_yml:
                        register_operand.input = reg_op_yml["input"]
                    if "ouput" in reg_op_yml:
                        register_operand.ouput = reg_op_yml["ouput"]
                    ec.register_operands.append(register_operand)

            instruction.execution_contexts.append(ec)

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

        string = string.replace("\n", "")
        return string
