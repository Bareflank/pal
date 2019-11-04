import abc
import itertools

from pal.logger import logger

class AbstractFilter(abc.ABC):
    @property
    @abc.abstractmethod
    def description(self):
        """ Description of what this filter does """

    @abc.abstractmethod
    def do_filter(self, reg):
        """ Filter the given register object """
        return

    def filter_exclusive(self, registers):
        """
        Filter the given registers such that registers matching the filter's
        criteria are excluded (removed)
        """
        logger.info("Applying filter: excluding {d}".format(d = str(self)))
        result = list(filter(self._do_filter, registers))
        logger.debug("{name} removed {count} registers".format(
            name = str(type(self).__name__),
            count = str(len(registers) - len(result))
        ))
        return result

    def filter_inclusive(self, registers):
        """
        Filter the given registers such that registers matching the filter's
        criteria are included, while all others are excluded (removed)
        """
        logger.info("Applying filter: including {d}".format(d = str(self)))
        result = list(itertools.filterfalse(self._do_filter, registers))
        logger.debug("{count} registers remaining after {name}".format(
            name = str(type(self).__name__),
            count = str(len(result))
        ))
        return result

    def _do_filter(self, reg):
        result = self.do_filter(reg)
        if result == False:
            logger.debug(str(type(self).__name__) + " matched: " + str(reg.name))
        return result

    def __str__(self):
        return self.description
