import abc
from typing import TextIO
from typing import List

from pal.model.register import Register
from pal.config import PalConfig


class PeripheralWriter(abc.ABC):

    @abc.abstractmethod
    def declare_peripheral_dependencies(self, outfile: TextIO, registers: List[Register], config: PalConfig) -> None:
        pass

    @abc.abstractmethod
    def declare_peripheral_views(self, outfile: TextIO, registers: List[Register]) -> None:
        pass
