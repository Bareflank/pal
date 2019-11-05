import abc
from typing import TextIO

from shoulder.model.register import Register
from shoulder.model.access_mechanism import AbstractAccessMechanism

class AccessMechanismWriter(abc.ABC):

    @abc.abstractmethod
    def declare_access_mechanism_dependencies(self, outfile: TextIO,
                                           register: Register) -> None:
        pass

    @abc.abstractmethod
    def call_readable_access_mechanism(
            self,
            outfile: TextIO,
            register: Register,
            access_mechanism: AbstractAccessMechanism,
            result: str
        ) -> None:
        pass

    @abc.abstractmethod
    def call_writable_access_mechanism(
            self,
            outfile: TextIO,
            register: Register,
            value: int,
            access_mechanism: AbstractAccessMechanism
        ) -> None:
        pass
