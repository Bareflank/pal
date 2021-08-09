import abc
from typing import TextIO

from pal.model.instruction import Instruction
from pal.config import PalConfig

class InstructionWriter(abc.ABC):

    @abc.abstractmethod
    def declare_instruction_dependencies(self, outfile: TextIO,
                                     instruction: Instruction, config: PalConfig) -> None:
        pass

    @abc.abstractmethod
    def declare_instruction_accessor(self, outfile: TextIO,
                                     instruction: Instruction) -> None:
        pass
