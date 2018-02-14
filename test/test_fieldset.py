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

from shoulder.fieldset import *
from shoulder.logger import logger

class TestFieldset(unittest.TestCase):

    def test_fieldset_init(self):
        self.assertIsNotNone(Fieldset(1))
        self.assertIsNotNone(Fieldset("1"))
        self.assertRaises(ValueError, Fieldset, "invalid")

    def test_fieldset__str(self):
        fs = Fieldset(32)
        fs.add_field("field", 31, 0)
        str(fs)
        fs.condition = "condition is true"
        str(fs)

    def test_fieldset_add_field(self):
        fs = Fieldset(32)
        fs.add_field("valid", 31, 0)
        self.assertRaises(ValueError, fs.add_field, "invalid1", "string", 0)
        self.assertRaises(ValueError, fs.add_field, "invalid1", 0, "string")
        self.assertRaises(ValueError, fs.add_field, "invalid1", "string", "string")

    def test_fieldset_is_valid(self):
        fs = Fieldset(32)
        self.assertFalse(fs.is_valid())

        fs = Fieldset(32)
        fs.add_field("field1", 31, 0)
        self.assertTrue(fs.is_valid())

        fs = Fieldset(32)
        fs.add_field("field1", 31, 0)
        fs.add_field("field2", 32, 32)
        self.assertFalse(fs.is_valid())

        fs = Fieldset(32)
        fs.add_field("field1", 31, 0)
        fs.add_field("field2", -1, -1)
        self.assertFalse(fs.is_valid())

        fs = Fieldset(32)
        fs.add_field("bit1", 31, 31)
        fs.add_field("bit1_duplicate", 31, 31)
        fs.add_field("field2", 30, 0)
        self.assertFalse(fs.is_valid())

        fs = Fieldset(32)
        fs.add_field("field1", 31, 20)
        fs.add_field("field1_duplicate", 31, 20)
        fs.add_field("field1", 19, 0)
        self.assertFalse(fs.is_valid())

        fs = Fieldset(32)
        fs.add_field("field1", 31, 20)
        fs.add_field("field1_overlap", 25, 0)
        self.assertFalse(fs.is_valid())

        fs = Fieldset(32)
        fs.add_field("field1", 31, 20)
        fs.add_field("field1_boundry_overlap", 20, 0)
        self.assertFalse(fs.is_valid())

        fs = Fieldset(32)
        fs.add_field("field1", 31, 20)
        fs.add_field("field1_adjacent", 19, 0)
        self.assertTrue(fs.is_valid())
