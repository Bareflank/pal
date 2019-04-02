#
# Shoulder
# Copyright (C) 2018 Assured Information Security, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import abc
import itertools

from shoulder.logger import logger

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
