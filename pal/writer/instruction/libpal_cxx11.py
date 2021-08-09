from pal.writer.instruction.instruction import InstructionWriter
from pal.model.instruction import Instruction
import pal.gadget

from typing import TextIO


class LibpalCxx11InstructionWriter(InstructionWriter):

    def declare_instruction_dependencies(self, outfile, instruction, config):
        self.__declare_header_includes(outfile, instruction)
        self.__declare_libpal_function_prototypes(outfile, instruction)

    def declare_instruction_accessor(self, outfile, instruction):
        self.__declare_instruction_comment(outfile, instruction)

        for execution_context in instruction.execution_contexts:
            self.__declare_accessor(outfile, instruction, execution_context)


    def __declare_header_includes(self, outfile, instruction):
        outfile.write("#include <stdint.h>")
        self.write_newline(outfile)
        outfile.write("#include <tuple>")
        self.write_newline(outfile, count=2)


    @pal.gadget.extern_c
    def __declare_libpal_function_prototypes(self, outfile, instruction):
        for execution_context in instruction.execution_contexts:
            self.__declare_libpal_c_return_type(outfile, instruction, execution_context)

            accessor = "{} pal_execute_{}{}({});".format(
                self.__get_libpal_return_type(instruction, execution_context),
                instruction.name.lower(),
                self.__get_execution_context_suffix(instruction, execution_context),
                self.__get_accessor_arg_string(instruction, execution_context)
            )

            outfile.write(accessor)
            self.write_newline(outfile)


    def __declare_instruction_comment(self, outfile, instruction):
        comment_text = "{} ({}){}".format(
            instruction.name,
            instruction.long_name,
            ": " + instruction.purpose if instruction.purpose else ""
        )
        self.declare_comment(outfile, comment_text, 79)


    def __declare_accessor(self, outfile, instruction, execution_context):
        function_name = "execute_{}{}".format(
            instruction.name.lower(),
            self.__get_execution_context_suffix(instruction, execution_context)
        )

        gadget = self.gadgets["pal.cxx.function_definition"]
        gadget.name = function_name
        gadget.return_type = self.__get_accessor_return_type(instruction, execution_context)
        gadget.args = self.__get_accessor_arg_list(instruction, execution_context)

        self.__declare_accessor_return_type(outfile, instruction, execution_context)
        self.__declare_accessor_details(outfile, instruction, execution_context)


    def __declare_accessor_return_type(self, outfile, instruction, execution_context):
        if len(execution_context.logical_outputs) > 1:
            type_declaration = "using {} = {};".format(
                self.__get_accessor_return_typedef_name(instruction, execution_context),
                self.__get_accessor_return_tuple(instruction, execution_context)
            )
            outfile.write(type_declaration)
            self.write_newline(outfile)


    @pal.gadget.cxx.function_definition
    def __declare_accessor_details(self, outfile, instruction, execution_context):
        if len(execution_context.logical_outputs) > 1:
            self.__declare_multi_return_accessor(outfile, instruction, execution_context)
        else:
            self.__declare_single_return_accessor(outfile, instruction, execution_context)


    def __declare_single_return_accessor(self, outfile, instruction, execution_context):
        args = self.__get_accessor_arg_list(instruction, execution_context)
        args_string = ', '.join([str(arg[1]) for arg in args])

        call_c_binding = "return pal_execute_{}{}({});".format(
            instruction.name.lower(),
            self.__get_execution_context_suffix(instruction, execution_context),
            args_string
        )

        outfile.write(call_c_binding)
        self.write_newline(outfile)


    def __declare_multi_return_accessor(self, outfile, instruction, execution_context):
        args = self.__get_accessor_arg_list(instruction, execution_context)
        args_string = ', '.join([str(arg[1]) for arg in args])

        call_c_binding = "{} output = pal_execute_{}{}({});".format(
            self.__get_libpal_return_type(instruction, execution_context),
            instruction.name.lower(),
            self.__get_execution_context_suffix(instruction, execution_context),
            args_string
        )

        outfile.write(call_c_binding)
        self.write_newline(outfile)

        return_statement = "return std::make_tuple({});".format(
            ", ".join("output." + lo.name.lower() for lo in execution_context.logical_outputs)
        )
        outfile.write(return_statement)


    def __declare_libpal_c_return_type(self, outfile, instruction, execution_context):
        if len(execution_context.logical_outputs) > 1:
            struct_name = self.__get_libpal_return_type(instruction, execution_context)
            outfile.write("typedef struct {} {{".format(struct_name))
            self.write_newline(outfile)

            for logical_output in execution_context.logical_outputs:
                struct_member = "{} {};".format(
                    self.__get_c_type_from_logical_operand(logical_output),
                    logical_output.name.lower()
                )
                self.write_indent(outfile)
                outfile.write(struct_member)
                self.write_newline(outfile)

            outfile.write("}} {};".format(struct_name))
            self.write_newline(outfile, count=2)


    def __get_libpal_return_type(self, instruction, execution_context):
        if len(execution_context.logical_outputs) > 1:
            return self.__get_libpal_c_return_structure_name(instruction, execution_context)
        elif len(execution_context.logical_outputs) == 1:
            return self.__get_c_type_from_logical_operand(execution_context.logical_outputs[0])
        else:
            return "void"


    def __get_libpal_c_return_structure_name(self, instruction, execution_context):
        return "pal_{}{}_return_values".format(
            instruction.name.lower(),
            self.__get_execution_context_suffix(instruction, execution_context)
        )


    def __get_accessor_return_type(self, instruction, execution_context):
        if len(execution_context.logical_outputs) > 1:
            return self.__get_accessor_return_typedef_name(instruction, execution_context)
        elif len(execution_context.logical_outputs) == 1:
            return self.__get_c_type_from_logical_operand(execution_context.logical_outputs[0])
        else:
            return "void"


    def __get_accessor_return_typedef_name(self, instruction, execution_context):
        return "{}{}_return_values".format(
            instruction.name.lower(),
            self.__get_execution_context_suffix(instruction, execution_context),
        )


    def __get_accessor_arg_list(self, instruction, execution_context):
        args = []

        if execution_context.logical_inputs:
            for idx, logical_input in enumerate(execution_context.logical_inputs):
                arg_type=self.__get_c_type_from_logical_operand(logical_input)
                arg_name=logical_input.name.lower()
                args.append((arg_type, arg_name))

        return args

    def __get_accessor_arg_string(self, instruction, execution_context):
        if not execution_context.logical_inputs:
            return "void"
        else:
            args = ""
            for idx, logical_input in enumerate(execution_context.logical_inputs):
                next_arg = "{arg_type} {arg_name}{comma}".format(
                    arg_type=self.__get_c_type_from_logical_operand(logical_input),
                    arg_name=logical_input.name.lower(),
                    comma="" if idx == len(execution_context.logical_inputs) - 1 else ", "
                )
                args = args + next_arg

        return args


    def __get_accessor_return_tuple(self, instruction, execution_context):
        return_types = [self.__get_c_type_from_logical_operand(lo) for lo in execution_context.logical_outputs]
        return "std::tuple<{}>".format(
            ", ".join(return_types)
        )

    def __get_execution_context_suffix(self, instruction, execution_context):
        if len(instruction.execution_contexts) > 1:
            return "_" + execution_context.execution_state.lower()
        else:
            return ""


    def __get_c_type_from_logical_operand(self, logical_operand):
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
