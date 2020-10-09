import abc
from typing import TextIO
from typing import List
from typing import Any

from pal.model.register import Register
from pal.model.fieldset import Fieldset
from pal.model.field import Field


class RegisterWriter(abc.ABC):

    @abc.abstractmethod
    def declare_register_dependencies(self, outfile: TextIO, register: Register) -> None:
        pass

    @abc.abstractmethod
    def declare_register_accessors(self, outfile: TextIO, register: Register) -> None:
        pass

    @abc.abstractmethod
    def declare_field_accessors(self, outfile: TextIO, register: Register,
                                field: Field) -> None:
        pass

    @abc.abstractmethod
    def declare_field_printers(outfile: TextIO, register: Register,
                                  field: Field):
        pass

    @abc.abstractmethod
    def declare_fieldset_printers(outfile: TextIO, register: Register,
                                  fieldset: Fieldset):
        pass

    @abc.abstractmethod
    def call_register_get(self, outfile: TextIO, register: Register,
                          destination: str, index: str=None) -> None:
        pass

    @abc.abstractmethod
    def call_field_get(self, outfile: TextIO, register: Register, field: Field,
                          destination: str, register_value: str) -> None:
        pass
