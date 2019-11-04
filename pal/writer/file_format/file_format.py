import abc
from typing import TextIO


class FileFormatWriter(abc.ABC):

    @abc.abstractmethod
    def write_newline(self, outfile: TextIO, count:int =1) -> None:
        pass

    @abc.abstractmethod
    def write_indent(self, outfile: TextIO, count:int =1) -> None:
        pass
