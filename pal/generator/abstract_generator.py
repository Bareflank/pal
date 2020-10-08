import abc
from typing import List
from typing import Dict
from pal.model.register import Register
from pal.model.instruction import Instruction
from pal.gadget.gadget_properties import GadgetProperties
from pal.gadget import create_gadget_properties

class AbstractGenerator(abc.ABC):
    def __init__(self, writer):
        self.writer = writer

    @abc.abstractmethod
    def generate_registers(self, registers: List[Register], outpath: str) -> None:
        """ Generate target output using the given registers """
        """ to the given output path """
        return

    @abc.abstractmethod
    def generate_instructions(self, instructions: List[Instruction], outpath: str) -> None:
        """ Generate target output using the given instructions """
        """ to the given output path """
        return

    @property
    def gadgets(self) -> List[GadgetProperties]:
        """ Returns a dictionary of gadget properties, keyed by gadget name """
        if not hasattr(self, "_gadgets"):
            self._gadgets = create_gadget_properties()
        return self._gadgets

    def get_writer(self):
        return self.writer
