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

from shoulder.filters.quirks import Quirks
from shoulder.register import *
from shoulder.fieldset import *
from shoulder.logger import logger

class TestQuirks(unittest.TestCase):

    def test_filter(self):
        regs = self._generate_test_register_set()
        expected_regs = self._generate_expected_register_set()
        f = Quirks()
        str(f)
        regs = f.do_filter(regs)

        self.assertTrue(len(regs) == len(expected_regs))
        for r_idx, r in enumerate(expected_regs):
            self.assertTrue(r.name == regs[r_idx].name)
            for fs_idx, fs in enumerate(r.fieldsets):
                self.assertTrue(len(fs.fields) == len(regs[r_idx].fieldsets[fs_idx].fields))

    def _generate_test_register_set(self):
        regs = []

        valid_r = Register()
        valid_r.name = "valid"
        fs = Fieldset(1)
        fs.add_field("1", 0, 0)
        valid_r.add_fieldset(fs)
        regs.append(valid_r)

        quirks_r1 = Register()
        quirks_r1.name = "FPEXC32_EL2"
        fs = Fieldset(1)
        fs.add_field("UFF", 0, 0)
        quirks_r1.add_fieldset(fs)
        regs.append(quirks_r1)

        quirks_r2 = Register()
        quirks_r2.name = "HCR_EL2"
        fs = Fieldset(1)
        fs.add_field("TPC", 0, 0)
        quirks_r2.add_fieldset(fs)
        regs.append(quirks_r2)

        quirks_r3 = Register()
        quirks_r3.name = "EDECCR"
        fs = Fieldset(2)
        fs.add_field("NSE", 0, 0)
        fs.add_field("SE", 1, 1)
        quirks_r3.add_fieldset(fs)
        regs.append(quirks_r3)

        return regs

    def _generate_expected_register_set(self):
        regs = []

        valid_r = Register()
        valid_r.name = "valid"
        valid_r.long_name = "a valid register, should not be filtered"
        valid_r.purpose = "test"
        valid_r.size = 1
        fs = Fieldset(1)
        fs.add_field("1", 0, 0)
        valid_r.add_fieldset(fs)
        regs.append(valid_r)

        quirks_r1 = Register()
        quirks_r1.name = "FPEXC32_EL2"
        fs = Fieldset(1)
        quirks_r1.add_fieldset(fs)
        regs.append(quirks_r1)

        quirks_r2 = Register()
        quirks_r2.name = "HCR_EL2"
        fs = Fieldset(1)
        quirks_r2.add_fieldset(fs)
        regs.append(quirks_r2)

        quirks_r3 = Register()
        quirks_r3.name = "EDECCR"
        fs = Fieldset(2)
        quirks_r3.add_fieldset(fs)
        regs.append(quirks_r3)

        return regs
