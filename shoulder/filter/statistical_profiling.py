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

from shoulder.filter.abstract_filter import AbstractFilter

class StatisticalProfilingRegisterFilter(AbstractFilter):
    def __init__(self):
        self.exclusions = [
            "pmsidr_el1",
            "pmsfcr_el1",
            "pmsicr_el1",
            "pmscr_el2",
            "pmbptr_el1",
            "pmbsr_el1",
            "pmsirr_el1",
            "pmscr_el1",
            "pmblimitr_el1",
            "pmslatfr_el1",
            "pmmir_el1"
        ]

    @property
    def description(self):
        return "statistical profiling registers"

    def do_filter(self, reg):
        if(reg.name.lower() in self.exclusions):
            return False
        else:
            return True
