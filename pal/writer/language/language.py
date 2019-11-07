import abc
from typing import TextIO
from typing import List
from typing import Any

from pal.model.register import Register
from pal.model.fieldset import Fieldset
from pal.model.field import Field


class LanguageWriter(abc.ABC):

    @abc.abstractmethod
    def declare_comment(self, outfile: TextIO, comment: str) -> None:
        pass

    @abc.abstractmethod
    def declare_register_dependencies(self, outfile: TextIO, register: Register) -> None:
        pass

    @abc.abstractmethod
    def declare_register_constants(self, outfile: TextIO, register: Register) -> None:
        pass

    @abc.abstractmethod
    def declare_register_get(self, outfile: TextIO, register: Register) -> None:
        pass

    @abc.abstractmethod
    def declare_register_set(self, outfile: TextIO, register: Register) -> None:
        pass

    @abc.abstractmethod
    def declare_field_constants(self, outfile: TextIO, register: Register,
                                field: Field) -> None:
        pass

    @abc.abstractmethod
    def declare_field_accessors(self, outfile: TextIO, register: Register,
                                field: Field) -> None:
        pass

    @abc.abstractmethod
    def call_register_get(self, outfile: TextIO, register: Register,
                          destination: str, index: str=None) -> None:
        pass

    @abc.abstractmethod
    def call_field_get(self, outfile: TextIO, register_value: str, field: Field,
                          destination: str) -> None:
        pass
