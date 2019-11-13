import abc
from typing import TextIO

from pal.model.register import Register
from pal.model.fieldset import Fieldset
from pal.model.field import Field


class PrinterWriter(abc.ABC):

    @abc.abstractmethod
    def declare_fieldset_printer(self, outfile: TextIO, register: Register,
                               fieldset: Fieldset) -> None:
        pass

    @abc.abstractmethod
    def declare_field_printer(self, outfile: TextIO, register: Register,
                            field: Field) -> None:
        pass
