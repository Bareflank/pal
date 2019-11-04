import abc

from pal.logger import logger

class AbstractTransform(abc.ABC):
    @property
    @abc.abstractmethod
    def description(self):
        """ Description of what this transform does """

    @abc.abstractmethod
    def do_transform(self, reg):
        """ Transform the given register object """
        return

    def transform(self, registers):
        """
        Transform the given list of registers
        """
        logger.info("Applying transform: {d}".format(d = str(self)))
        return list(map(self.do_transform, registers))

    def __str__(self):
        return self.description
