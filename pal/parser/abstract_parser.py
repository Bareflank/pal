import abc
import typing

from pal.model.register import Register


class AbstractParser(abc.ABC):
    @abc.abstractmethod
    def parse_file(self, file_path: str) -> typing.List[Register]:
        """ Parse the file at the given path to a list of register objects """
        return
