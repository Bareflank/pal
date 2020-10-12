import abc
from typing import TextIO

from pal.model.instruction import Instruction

class InstructionWriter(abc.ABC):

    @abc.abstractmethod
    def declare_instruction_accessor(self, outfile: TextIO,
                                     instruction: Instruction) -> None:
        pass
