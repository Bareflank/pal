import abc
from typing import TextIO


class CommentWriter(abc.ABC):

    @abc.abstractmethod
    def declare_comment(self, outfile: TextIO, comment: str, wrap: int) -> None:
        pass
