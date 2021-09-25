import abc
from typing import TextIO


class CommentWriter(abc.ABC):

    @abc.abstractmethod
    def declare_comment(self, outfile: TextIO, comment: str, wrap: int) -> None:
        pass

    @abc.abstractmethod
    def declare_file_documentation(self, outfile: TextIO, summary: str, wrap: int, details: str="") -> None:
        pass

    @abc.abstractmethod
    def declare_item_documentation(self, outfile: TextIO, summary: str, wrap: int, details: str="") -> None:
        pass
