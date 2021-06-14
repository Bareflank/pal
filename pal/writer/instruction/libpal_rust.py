from pal.writer.instruction.instruction import InstructionWriter
from pal.model.instruction import Instruction
import pal.gadget

from typing import TextIO


class LibpalRustInstructionWriter(InstructionWriter):

    def declare_instruction_dependencies(self, outfile, instruction):
        ctypes = set([])
        for ec in instruction.execution_contexts:
            for logical_input in ec.logical_inputs:
                ctypes.add(self.__get_c_type_from_logical_operand(logical_input))
            for logical_output in ec.logical_outputs:
                ctypes.add(self.__get_c_type_from_logical_operand(logical_output))

        for ctype in ctypes:
            if not ctype == "bool":
                outfile.write("use cty::{};".format(ctype))
                self.write_newline(outfile)

        self.write_newline(outfile)

    def declare_instruction_accessor(self, outfile, instruction):
        self.__declare_accessor_comment(outfile, instruction)
        self.write_newline(outfile)

        for ec in instruction.execution_contexts:
            if len(ec.logical_outputs) > 1:
                self.__declare_return_data_structure(outfile, instruction, ec)
                self.write_newline(outfile)

            self.__declare_libpal_c_function_prototype(outfile, instruction, ec)
            self.write_newline(outfile)
            self.__declare_rust_accessor_function(outfile, instruction, ec)


    def __declare_accessor_comment(self, outfile, instruction):
        comment_text = "{name} ({long_name}){purpose}".format(
            name=instruction.name,
            long_name=instruction.long_name,
            purpose=": " + instruction.purpose if instruction.purpose else ""
        )
        self.declare_comment(outfile, comment_text, 79)


    def __declare_return_data_structure(self, outfile, instruction, execution_context):
        outfile.write("#[repr(C)]")
        self.write_newline(outfile)

        struct_name = self.__get_return_struct_name(instruction, execution_context)
        struct_declaration = "struct {name} {{".format(
            name=struct_name
        )
        outfile.write(struct_declaration)
        self.write_newline(outfile)

        for logical_output in execution_context.logical_outputs:
            struct_member = "{member_name}: {c_type},".format(
                c_type=self.__get_c_type_from_logical_operand(logical_output),
                member_name=logical_output.name.lower()
            )
            self.write_indent(outfile)
            outfile.write(struct_member)
            self.write_newline(outfile)

        outfile.write("}}".format(name=struct_name))
        self.write_newline(outfile)

    @pal.gadget.rust.extern
    def __declare_libpal_c_function_prototype(self, outfile, instruction,
                                             execution_context):
        accessor = "fn pal_execute_{}{}({}) -> {};".format(
            instruction.name.lower(),
            self.__get_execution_context_suffix(instruction, execution_context),
            self.__get_c_accessor_arg_string(instruction, execution_context),
            self.__get_libpal_return_type(instruction, execution_context)
        )

        outfile.write(accessor)
        self.write_newline(outfile)


    def __declare_rust_accessor_function(self, outfile, instruction,
                                         execution_context):
        accessor = "pub fn execute_{inst_name}{ec_name}({args}) -> {rtype} {{".format(
            inst_name=instruction.name.lower(),
            ec_name="_" + execution_context.execution_state.lower() if len(instruction.execution_contexts) > 1 else "",
            args=self.__get_rust_accessor_arg_string(instruction, execution_context),
            rtype=self.__get_rust_accessor_return_type(instruction, execution_context)
        )
        outfile.write(accessor)
        self.write_newline(outfile)

        gadget = self.gadgets["pal.rust.unsafe"]
        gadget.indent = 1
        self.__declare_rust_accessor_function_details(outfile, instruction, execution_context)

        outfile.write("}")
        self.write_newline(outfile)


    @pal.gadget.rust.unsafe
    def __declare_rust_accessor_function_details(self, outfile, instruction,
                                                 execution_context):
        inputs = [i.name.lower() for i in execution_context.logical_inputs]
        outputs = [o.name.lower() for o in execution_context.logical_outputs]

        if len(execution_context.logical_outputs) > 1:
            outfile.write("let outputs = pal_execute_{}{}({});".format(
                instruction.name.lower(),
                self.__get_execution_context_suffix(instruction, execution_context),
                ", ".join(inputs)
            ))
            self.write_newline(outfile)

            tuple_values = ""
            outfile.write("({})".format(
                ", ".join(["outputs." + name for name in outputs])
            ))
            self.write_newline(outfile)
        else:
            outfile.write("pal_execute_{}{}({})".format(
                instruction.name.lower(),
                self.__get_execution_context_suffix(instruction, execution_context),
                ", ".join(inputs)
            ))

    def __get_accessor_return_type(self, instruction, execution_context):
        if len(execution_context.logical_outputs) > 1:
            return self.__get_return_struct_name(instruction, execution_context)
        elif len(execution_context.logical_outputs) == 1:
            return self.__get_rust_type_from_logical_operand(execution_context.logical_outputs[0])
        else:
            return "()"


    def __get_libpal_return_type(self, instruction, execution_context):
        if len(execution_context.logical_outputs) > 1:
            return self.__get_libpal_c_return_structure_name(instruction, execution_context)
        elif len(execution_context.logical_outputs) == 1:
            return self.__get_c_type_from_logical_operand(execution_context.logical_outputs[0])
        else:
            return "()"


    def __get_libpal_c_return_structure_name(self, instruction, execution_context):
        return "{}{}_return_values".format(
            instruction.name.lower(),
            self.__get_execution_context_suffix(instruction, execution_context)
        )


    def __get_rust_accessor_return_type(self, instruction, execution_context):
        if len(execution_context.logical_outputs) > 1:
            return self.__get_rust_return_tuple(instruction, execution_context)
        elif len(execution_context.logical_outputs) == 1:
            return self.__get_rust_type_from_logical_operand(execution_context.logical_outputs[0])
        else:
            return "()"


    def __get_rust_return_tuple(self, instruction, execution_context):
        tuple_types = ""

        for idx, logical_output in enumerate(execution_context.logical_outputs):
            next_arg = "{arg_type}{comma}".format(
                arg_type=self.__get_rust_type_from_logical_operand(logical_output),
                comma="" if idx == len(execution_context.logical_outputs) - 1 else ", "
            )
            tuple_types = tuple_types + next_arg

        return "({})".format(tuple_types)


    def __get_rust_accessor_arg_string(self, instruction, execution_context):
        if not execution_context.logical_inputs:
            return ""
        else:
            args = ""
            for idx, logical_input in enumerate(execution_context.logical_inputs):
                next_arg = "{arg_name}: {arg_type}{comma}".format(
                    arg_name=logical_input.name.lower(),
                    arg_type=self.__get_rust_type_from_logical_operand(logical_input),
                    comma="" if idx == len(execution_context.logical_inputs) - 1 else ", "
                )
                args = args + next_arg

        return args


    def __get_c_accessor_arg_string(self, instruction, execution_context):
        if not execution_context.logical_inputs:
            return ""
        else:
            args = ""
            for idx, logical_input in enumerate(execution_context.logical_inputs):
                next_arg = "{arg_name}: {arg_type}{comma}".format(
                    arg_type=self.__get_c_type_from_logical_operand(logical_input),
                    arg_name=logical_input.name.lower(),
                    comma="" if idx == len(execution_context.logical_inputs) - 1 else ", "
                )
                args = args + next_arg

        return args


    def __get_return_struct_name(self, instruction, execution_context):
        return "{inst_name}{ec_name}_return_values".format(
            inst_name=instruction.name.lower(),
            ec_name="_" + execution_context.execution_state.lower() if len(instruction.execution_contexts) > 1 else ""
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
            return "()"


    def __get_rust_type_from_logical_operand(self, logical_operand):
        rust_types = {
            "int8": "i8",
            "int16": "i16",
            "int32": "i32",
            "int64": "i64",
            "uint8": "u8",
            "uint16": "u16",
            "uint32": "u32",
            "uint64": "u64",
            "boolean": "bool"
        }

        if logical_operand.type in rust_types:
            return rust_types[logical_operand.type]
        else:
            return "()"
