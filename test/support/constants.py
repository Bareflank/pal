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

import os

from shoulder.register import Register
from shoulder.fieldset import Fieldset

TEST_CONSTANTS_PATH = os.path.dirname(os.path.realpath(__file__))
TEST_TOP_DIR = os.path.join(TEST_CONSTANTS_PATH, os.pardir)
TEST_SUPPORT_DIR = os.path.join(TEST_TOP_DIR, "support")

TEST_CONFIG_FILE_PATH = os.path.join(TEST_SUPPORT_DIR, "testshoulderconfig.py")

# -----------------------------------------------------------------------------
# Test XML Register Files and Expected Values
# -----------------------------------------------------------------------------

TEST_XML_REG32_PATH = os.path.join(TEST_SUPPORT_DIR, "mock_register_32.xml")
TEST_XML_REG32 = Register()
TEST_XML_REG32.name = "MOCK_REGISTER"
TEST_XML_REG32.long_name = "A mock 32-bit register for testing shoulder"
TEST_XML_REG32.purpose = "Register does not belong to the aarch64 architecture"
TEST_XML_REG32.size = 32
TEST_XML_REG32.is_sysreg = True
TEST_XML_REG32_FIELDSET = Fieldset(TEST_XML_REG32.size)
TEST_XML_REG32_FIELDSET.add_field("msb", 31, 31)
TEST_XML_REG32_FIELDSET.add_field("not_msb_lsb", 30, 1)
TEST_XML_REG32_FIELDSET.add_field("lsb", 0, 0)
TEST_XML_REG32.add_fieldset(TEST_XML_REG32_FIELDSET)

TEST_XML_REG64_PATH = os.path.join(TEST_SUPPORT_DIR, "mock_register_64.xml")
TEST_XML_REG64 = Register()
TEST_XML_REG64.name = "MOCK_REGISTER"
TEST_XML_REG64.long_name = "A mock 64-bit register for testing shoulder"
TEST_XML_REG64.purpose = "Register does not belong to the aarch64 architecture"
TEST_XML_REG64.size = 64
TEST_XML_REG64.is_sysreg = True
TEST_XML_REG64_FIELDSET = Fieldset(TEST_XML_REG64.size)
TEST_XML_REG64_FIELDSET.add_field("msb", 63, 63)
TEST_XML_REG64_FIELDSET.add_field("not_msb_lsb", 62, 1)
TEST_XML_REG64_FIELDSET.add_field("lsb", 0, 0)
TEST_XML_REG64.add_fieldset(TEST_XML_REG64_FIELDSET)

TEST_XML_MULTIPLE_FIELDSETS_PATH = os.path.join(TEST_SUPPORT_DIR, "mock_register_multiple_fieldsets.xml")
TEST_XML_MULTIPLE_FIELDSETS = Register()
TEST_XML_MULTIPLE_FIELDSETS.name = "MOCK_REGISTER_MULTIPLE_FIELDSETS"
TEST_XML_MULTIPLE_FIELDSETS.long_name = "A mock 64-bit register with multiple fields"
TEST_XML_MULTIPLE_FIELDSETS.purpose = "Register does not belong to the aarch64 architecture"
TEST_XML_MULTIPLE_FIELDSETS.size = 64
TEST_XML_MULTIPLE_FIELDSETS.is_sysreg = True
TEST_XML_MULTIPLE_FIELDSETS_FIELDSET = Fieldset(TEST_XML_MULTIPLE_FIELDSETS.size)
TEST_XML_MULTIPLE_FIELDSETS_FIELDSET.condition = "the condition under which this fieldset is used"
TEST_XML_MULTIPLE_FIELDSETS_FIELDSET.add_field("msb", 63, 63)
TEST_XML_MULTIPLE_FIELDSETS_FIELDSET.add_field("not_msb_lsb", 62, 1)
TEST_XML_MULTIPLE_FIELDSETS_FIELDSET.add_field("lsb", 0, 0)
TEST_XML_MULTIPLE_FIELDSETS.add_fieldset(TEST_XML_MULTIPLE_FIELDSETS_FIELDSET)
TEST_XML_MULTIPLE_FIELDSETS_FIELDSET = Fieldset(TEST_XML_MULTIPLE_FIELDSETS.size)
TEST_XML_MULTIPLE_FIELDSETS_FIELDSET.condition = "the condition under which this other fieldset is used"
TEST_XML_MULTIPLE_FIELDSETS_FIELDSET.add_field("upper_half", 63, 22)
TEST_XML_MULTIPLE_FIELDSETS_FIELDSET.add_field("lower_half", 21, 0)
TEST_XML_MULTIPLE_FIELDSETS.add_fieldset(TEST_XML_MULTIPLE_FIELDSETS_FIELDSET)

TEST_XML_NAME_ONLY_PATH = os.path.join(TEST_SUPPORT_DIR, "mock_register_name_only.xml")
TEST_XML_NAME_ONLY = Register()
TEST_XML_NAME_ONLY.name = "NAME_ONLY_REGISTER"
TEST_XML_NAME_ONLY.long_name = None
TEST_XML_NAME_ONLY.purpose = None
TEST_XML_NAME_ONLY.size = None
TEST_XML_NAME_ONLY.is_sysreg = True
TEST_XML_NAME_ONLY_FIELDSET = []

TEST_XML_INVALID_FIELD_PATH = os.path.join(TEST_SUPPORT_DIR, "mock_register_invalid_field.xml")
TEST_XML_INVALID_FIELD = Register()
TEST_XML_INVALID_FIELD.name = "MOCK_REGISTER_INVALID_FIELD"
TEST_XML_INVALID_FIELD.long_name = "A mock 64-bit register with an invalid field"
TEST_XML_INVALID_FIELD.purpose = None
TEST_XML_INVALID_FIELD.size = 64
TEST_XML_INVALID_FIELD.is_sysreg = True
TEST_XML_INVALID_FIELD_FIELDSET = []

TEST_XML_MULTIPLE_PURPOSE_PATH = os.path.join(TEST_SUPPORT_DIR, "mock_register_multiple_purpose.xml")

TEST_XML_NO_ATTRIBUTES_PATH = os.path.join(TEST_SUPPORT_DIR, "mock_register_no_attributes.xml")

TEST_XML_EMPTY_PATH = os.path.join(TEST_SUPPORT_DIR, "mock_register_empty.xml")
