from pal.writer.instruction.instruction import InstructionWriter
from pal.model.instruction import Instruction

from typing import TextIO


class LibpalCInstructionWriter(InstructionWriter):

    def declare_instruction_accessor(self, outfile: TextIO, instruction: Instruction) -> None:
        self._declare_accessor_comment(outfile, instruction)

        for execution_context in instruction.execution_contexts:
            if len(execution_context.logical_outputs) > 1:
                self._declare_return_data_structure(outfile, instruction,
                                                    execution_context)

            accessor = "{rtype} pal_execute_{inst_name}{ec_name}({args});".format(
                rtype=self._get_accessor_return_type(instruction, execution_context),
                inst_name=instruction.name.lower(),
                ec_name="_" + execution_context.execution_state.lower() if len(instruction.execution_contexts) > 1 else "",
                args=self._get_accessor_args(instruction, execution_context)
            )

            outfile.write(accessor)
            self.write_newline(outfile)


    def _declare_accessor_comment(self, outfile, instruction):
        comment_text = "{name} ({long_name}){purpose}".format(
            name=instruction.name,
            long_name=instruction.long_name,
            purpose=": " + instruction.purpose if instruction.purpose else ""
        )
        self.declare_comment(outfile, comment_text, 79)


    def _declare_return_data_structure(self, outfile, instruction, execution_context):
        struct_name = self._get_return_struct_name(instruction, execution_context)
        struct_declaration = "typedef struct {name} {{".format(
            name=struct_name
        )
        outfile.write(struct_declaration)
        self.write_newline(outfile)

        for logical_output in execution_context.logical_outputs:
            struct_member = "{c_type} {member_name};".format(
                c_type=self._get_c_type_from_logical_operand(logical_output),
                member_name=logical_output.name.lower()
            )
            self.write_indent(outfile)
            outfile.write(struct_member)
            self.write_newline(outfile)

        outfile.write("}} {name};".format(name=struct_name))
        self.write_newline(outfile, count=2)

    def _get_accessor_return_type(self, instruction, execution_context):
        if len(execution_context.logical_outputs) > 1:
            return self._get_return_struct_name(instruction, execution_context)
        elif len(execution_context.logical_outputs) == 1:
            return self._get_c_type_from_logical_operand(execution_context.logical_outputs[0])
        else:
            return "void"

    def _get_accessor_args(self, instruction, execution_context):
        if not execution_context.logical_inputs:
            return "void"
        else:
            args = ""
            for idx, logical_input in enumerate(execution_context.logical_inputs):
                next_arg = "{arg_type} {arg_name}{comma}".format(
                    arg_type=self._get_c_type_from_logical_operand(logical_input),
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
