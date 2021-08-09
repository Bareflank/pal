from pal.writer.instruction.instruction import InstructionWriter
from pal.model.instruction import Instruction
import pal.gadget

from typing import TextIO


class GnuInlineInstructionWriter(InstructionWriter):

    def declare_instruction_dependencies(self, outfile, instruction, config):
        if config.stdint_header:
            outfile.write('#include "' + str(config.stdint_header) + '"')
        else:
            outfile.write("#include <stdint.h>")
        self.write_newline(outfile)

        outfile.write('#include "{name}_inline.h"'.format(
            name=instruction.name.lower()
        ))
        self.write_newline(outfile)

    def declare_instruction_accessor(self, outfile, instruction):
        self._declare_accessor_comment(outfile, instruction)

        for execution_context in instruction.execution_contexts:
            gadget = self.gadgets["pal.c.function_definition"]
            gadget.name = "pal_execute_{inst_name}{ec_name}".format(
                inst_name=instruction.name.lower(),
                ec_name="_" + execution_context.execution_state.lower() if len(instruction.execution_contexts) > 1 else "",
            )
            gadget.return_type = self._get_accessor_return_type(instruction, execution_context)
            gadget.args = self._get_accessor_gadget_args(instruction, execution_context)


            self._declare_instruction_accessor_details(outfile, instruction, execution_context)

    @pal.gadget.c.function_definition
    def _declare_instruction_accessor_details(self, outfile, instruction, execution_context):
        outfile.write("{ret}pal_execute_{inst_name}{ec_name}_inline({args});".format(
            ret="return " if execution_context.logical_outputs else "",
            inst_name=instruction.name.lower(),
            ec_name="_" + execution_context.execution_state.lower() if len(instruction.execution_contexts) > 1 else "",
            args=self._get_accessor_args(instruction, execution_context)
        ))


    def _declare_accessor_comment(self, outfile, instruction):
        comment_text = "{name} ({long_name}){purpose}".format(
            name=instruction.name,
            long_name=instruction.long_name,
            purpose=": " + instruction.purpose if instruction.purpose else ""
        )
        self.declare_comment(outfile, comment_text, 79)

    def _get_accessor_return_type(self, instruction, execution_context):
        if len(execution_context.logical_outputs) > 1:
            return self._get_return_struct_name(instruction, execution_context)
        elif len(execution_context.logical_outputs) == 1:
            return self._get_c_type_from_logical_operand(execution_context.logical_outputs[0])
        else:
            return "void"

    def _get_accessor_gadget_args(self, instruction, execution_context):
        args = []

        for idx, logical_input in enumerate(execution_context.logical_inputs):
            arg_type = self._get_c_type_from_logical_operand(logical_input)
            arg_name = logical_input.name.lower()
            args.append((arg_type, arg_name))

        return args

    def _get_accessor_args(self, instruction, execution_context):
        args = ""
        for idx, logical_input in enumerate(execution_context.logical_inputs):
            next_arg = "{arg_name}{comma}".format(
                arg_name=logical_input.name.lower(),
                comma="" if idx == len(execution_context.logical_inputs) - 1 else ", "
            )
            args = args + next_arg

        return args

    def _get_return_struct_name(self, instruction, execution_context):
        return "pal_{inst_name}{ec_name}_return_values".format(
            inst_name=instruction.name.lower(),
            ec_name="_" + execution_context.execution_state.lower() if len(instruction.execution_contexts) > 1 else ""
        )

    def _get_c_type_from_logical_operand(self, logical_operand):
        c_types = {
            "int8": "int8_t",
            "int16": "int16_t",
            "int32": "int32_t",
            "int64": "int64_t",
            "uint8": "uint8_t",
            "uint16": "uint16_t",
            "uint32": "uint32_t",
            "uint64": "uint64_t",
            "boolean": "bool"
        }

        if logical_operand.type in c_types:
            return c_types[logical_operand.type]
        else:
            return "void"
