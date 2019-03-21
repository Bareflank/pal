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

from shoulder.filters.abstract_filter import AbstractFilter
from shoulder.logger import logger

class NCounterToZero(AbstractFilter):
    @property
    def description(self):
        d = "Replacing '<n>' with '0'"
        return d

    def do_filter(self, objects):
        result = list(map(self._do_single_transform, objects))
        return result

    def _do_single_transform(self, reg):
        new_name = reg.name.replace("<n>", "0")
        if new_name != reg.name:
            logger.debug("Replaced '<n>' in register: {name} -> {new_name}".format(
                name = reg.name,
                new_name = new_name
            ))

            reg.name = new_name

        for fs in reg.fieldsets:
            for f in fs.fields:
                new_name = f.name.replace("<n>", "0")
                if new_name != f.name:
                    logger.debug("Replaced '<n>' in field: {name} -> {new_name}".format(
                        name = f.name,
                        new_name = new_name
                    ))
                    f.name = new_name

        new_access_mnemonic = reg.access_mnemonic.replace("<n>", "0")
        if new_access_mnemonic != reg.access_mnemonic:
            logger.debug("Replaced '<n>' in register: {name} -> {new_name}".format(
                name = reg.name,
                new_name = new_name
            ))
            reg.access_mnemonic = new_access_mnemonic

        return reg
