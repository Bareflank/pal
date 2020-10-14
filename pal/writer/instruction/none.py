from pal.writer.instruction.instruction import InstructionWriter
from pal.model.instruction import Instruction

from typing import TextIO


class NoneInstructionWriter(InstructionWriter):

    def declare_instruction_dependencies(self, outfile, instruction):
        pass

    def declare_instruction_accessor(self, outfile: TextIO,
                                     instruction: Instruction) -> None:
        pass
