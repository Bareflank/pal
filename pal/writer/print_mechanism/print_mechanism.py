import abc
from typing import TextIO

from pal.model.register import Register
from pal.model.field import Field


class PrintMechanismWriter(abc.ABC):

    @abc.abstractmethod
    def declare_print_mechanism_dependencies(self, outfile: TextIO,
                                             register: Register) -> None:
        pass

    @abc.abstractmethod
    def print_value_as_register(self, outfile: TextIO, register: Register,
                                value: str) -> None:
        pass

    @abc.abstractmethod
    def print_value_as_field(self, outfile: TextIO, register: Register,
                             field: Field, value: str) -> None:
        pass
