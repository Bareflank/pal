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

class MiscelaneousRegisterFilter(AbstractFilter):
    def __init__(self):
        self.exclusions = [
            "ccsidr2_el1",
            "id_pfr2_el1",
            "id_isar6_el1",
            "pmmir_el1",
            "erxmisc2_el1",
            "tfsr_el3",
            "erxpfgcdn_el1",
            "rndr",
            "erxpfgctl_el1",
            "tfsr_el2",
            "s3_<op1>_c<cn>_c<cm>_<op2>",
            "erxmisc3_el1",
            "tfsre0_el1",
            "ssbs",
            "erxpfgf_el1",
            "rndrrs",
            "tfsr_el1",
            "tco",
            "gcr_el1",
            "rgsr_el1"
        ]

    @property
    def description(self):
        return "Removing miscelaneous not-yet-supported registers"

    def do_filter(self, objects):
        result = list(filter(self._do_single_filter, objects))
        return result

    def _do_single_filter(self, reg):
        if(reg.name.lower() in self.exclusions):
            return False
        elif(reg.name.lower().startswith("s3_")):
            return False
        else:
            return True
