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

class RemoveReservedFields(AbstractFilter):
    @property
    def description(self):
        d = "Removing fields with reserved keywords (\"0\", \"1\", \"RES\", "
        d += "\"IMPLEMENTATION DEFINED\", etc.)"
        return d

    def do_filter(self, objects):
        result = list(map(self._do_single_transform, objects))
        return result

    def _do_single_transform(self, reg):
        for fs in reg.fieldsets:
            fs_len = len(fs.fields)
            fs.fields = [field for field in fs.fields if not "0" == field.name]
            fs.fields = [field for field in fs.fields if not "1" == field.name]
            fs.fields = [field for field in fs.fields if not "res" in field.name.lower()]
            fs.fields = [field for field in fs.fields if not "implementation defined" == field.name.lower()]

            count = fs_len - len(fs.fields)
            if count:
                logger.debug("Removed {count} reserved field{s} from {reg}".format(
                    count = count,
                    reg = reg.name,
                    s = "" if count == 1 else "s"
                ))

        return reg
