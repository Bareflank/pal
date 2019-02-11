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
import sys

from shoulder.filters.special_to_underscore import SpecialToUnderscore
from shoulder.register import *
from shoulder.fieldset import *
from shoulder.logger import logger

class TestRemoveInvalidRegisters(unittest.TestCase):

    def test_filter(self):
        regs = self._generate_test_register_set()
        expected_regs = self._generate_expected_register_set()
        f = SpecialToUnderscore()
        regs = f.do_filter(regs)
        str(f)

        self.assertTrue(len(regs) == len(expected_regs))
        for r_idx, r in enumerate(expected_regs):
            self.assertTrue(r.name == regs[r_idx].name)
            self.assertTrue(r.fieldsets[0].fields[0].name == regs[r_idx].fieldsets[0].fields[0].name)

    def _generate_test_register_set(self):
        regs = []

        r = Register()
        r.name = "test<0>"
        fs = Fieldset(1)
        fs.add_field("field<1>", 0, 0)
        r.add_fieldset(fs)
        regs.append(r)

        r = Register()
        r.name = "test[0]"
        fs = Fieldset(1)
        fs.add_field("field[1]", 0, 0)
        r.add_fieldset(fs)
        regs.append(r)

        r = Register()
        r.name = "test{0}"
        fs = Fieldset(1)
        fs.add_field("field{1}", 0, 0)
        r.add_fieldset(fs)
        regs.append(r)

        r = Register()
        r.name = "test(0)"
        fs = Fieldset(1)
        fs.add_field("field(1)", 0, 0)
        r.add_fieldset(fs)
        regs.append(r)

        return regs

    def _generate_expected_register_set(self):
        regs = []

        valid_r = Register()
        valid_r.name = "test_0_"
        fs = Fieldset(1)
        fs.add_field("field_1_", 0, 0)
        valid_r.add_fieldset(fs)

        regs.append(valid_r)
        regs.append(valid_r)
        regs.append(valid_r)
        regs.append(valid_r)

        return regs
