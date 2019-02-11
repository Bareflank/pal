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
import unittest

from shoulder.filters import *
from shoulder.register import *
from shoulder.fieldset import *
from shoulder.logger import logger

class TestFiltersInit(unittest.TestCase):

    def test_apply_filters(self):
        all_filters = [cls for cls in abstract_filter.AbstractFilter.__subclasses__()]
        filters_count = len(all_filters)

        regs = self._generate_test_register_set()
        regs = apply_filters(regs)

        # TODO: parse the logger output to verify that all filters have been applied
        # applied_count = parse_the_logger_output()
        # self.assertTrue(filters_count == applied_count)

    def _generate_test_register_set(self):
        regs = []

        valid_r = Register()
        valid_r.name = "register"

        return regs
