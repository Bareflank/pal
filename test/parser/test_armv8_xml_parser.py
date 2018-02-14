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
import os
import glob
import sys

from lxml import etree as ET

from shoulder.parser.armv8_xml_parser import *
from shoulder.exception import *
from test.support.constants import *
from shoulder.config import config

class TestArmV8XmlParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.parser = ArmV8XmlParser()
        logger.set_log_level("silent")

    @classmethod
    def tearDownClass(cls):
        logger.set_log_level(config.log_level)

    def _assert_fieldsets_equal(self, fs1, fs2):
        self.assertEqual(len(fs1), len(fs2))
        for fs_idx, fs in enumerate(fs1):
            self.assertEqual(len(fs.fields), len(fs2[fs_idx].fields))
            for f_idx, f in enumerate(fs.fields):
                self.assertEqual(f.name, fs2[fs_idx].fields[f_idx].name)
                self.assertEqual(f.msb, fs2[fs_idx].fields[f_idx].msb)
                self.assertEqual(f.lsb, fs2[fs_idx].fields[f_idx].lsb)

    def _assert_registers_equal(self, regs1, regs2):
        self.assertEqual(len(regs1), len(regs2))
        for r_idx, r in enumerate(regs1):
            self.assertEqual(r.name, regs2[r_idx].name)
            self.assertEqual(r.long_name, regs2[r_idx].long_name)
            self.assertEqual(r.purpose, regs2[r_idx].purpose)
            self.assertEqual(r.size, regs2[r_idx].size)
            self.assertEqual(r.is_sysreg, regs2[r_idx].is_sysreg)
            self._assert_fieldsets_equal(r.fieldsets, regs2[r_idx].fieldsets)

    def test_parser_init(self):
        self.assertIsNotNone(self.parser)

    def test_parser_properties(self):
        self.assertEqual(self.parser.aarch_version_major, 8)
        self.assertEqual(self.parser.aarch_version_minor, None)

    def test_parse_registers(self):
        regs = self.parser.parse_registers(TEST_XML_REG32_PATH)
        expected_regs = [TEST_XML_REG32]
        self._assert_registers_equal(regs, expected_regs)

        regs = self.parser.parse_registers(TEST_XML_REG64_PATH)
        expected_regs = [TEST_XML_REG64]
        self._assert_registers_equal(regs, expected_regs)

        regs = self.parser.parse_registers(TEST_XML_NAME_ONLY_PATH)
        expected_regs = [TEST_XML_NAME_ONLY]
        self._assert_registers_equal(regs, expected_regs)

        self.assertRaises(ShoulderParserException, self.parser.parse_registers, TEST_XML_NO_ATTRIBUTES_PATH)
        self.assertRaises(ShoulderParserException, self.parser.parse_registers, TEST_XML_EMPTY_PATH)
        self.assertRaises(ShoulderParserException, self.parser.parse_registers, "")

    def test__set_register_name(self):
        r = Register()
        etree = ET.parse(TEST_XML_NAME_ONLY_PATH)
        reg_node = etree.getroot().find("./registers/register")
        self.parser._set_register_name(r, reg_node)
        self.assertEqual(r.name, TEST_XML_NAME_ONLY.name)

    def test__set_register_long_name(self):
        r = Register()
        etree = ET.parse(TEST_XML_REG64_PATH)
        reg_node = etree.getroot().find("./registers/register")
        self.parser._set_register_long_name(r, reg_node)
        self.assertEqual(r.long_name, TEST_XML_REG64.long_name)

    def test__set_register_purpose(self):
        r = Register()
        etree = ET.parse(TEST_XML_REG64_PATH)
        reg_node = etree.getroot().find("./registers/register")
        self.parser._set_register_purpose(r, reg_node)
        self.assertEqual(r.purpose, TEST_XML_REG64.purpose)

        etree = ET.parse(TEST_XML_MULTIPLE_PURPOSE_PATH)
        reg_node = etree.getroot().find("./registers/register")
        self.parser._set_register_purpose(r, reg_node)
        expected_text = "See the ARMv" + str(self.parser.aarch_version_major)
        if self.parser.aarch_version_minor is not None:
            expected_text += "." + str(self.parser.aarch_version_minor)
        expected_text += " architecture reference manual for a description"
        expected_text += " of this register"
        self.assertEqual(r.purpose, expected_text)

    def test__set_register_size(self):
        r = Register()
        etree = ET.parse(TEST_XML_REG64_PATH)
        reg_node = etree.getroot().find("./registers/register")
        self.parser._set_register_size(r, reg_node)
        self.assertEqual(r.size, TEST_XML_REG64.size)

    def test__set_register_fields(self):
        # Single fieldset
        r = Register()
        r.size = 64
        etree = ET.parse(TEST_XML_REG64_PATH)
        reg_node = etree.getroot().find("./registers/register")
        self.parser._set_register_fields(r, reg_node)
        self.assertEqual(len(r.fieldsets), len(TEST_XML_REG64.fieldsets))
        for fs_idx, fs in enumerate(r.fieldsets):
            self.assertEqual(len(fs.fields), len(TEST_XML_REG64.fieldsets[fs_idx].fields))
            for f_idx, f in enumerate(fs.fields):
                self.assertEqual(f.name, TEST_XML_REG64.fieldsets[fs_idx].fields[f_idx].name)
                self.assertEqual(f.msb, TEST_XML_REG64.fieldsets[fs_idx].fields[f_idx].msb)
                self.assertEqual(f.lsb, TEST_XML_REG64.fieldsets[fs_idx].fields[f_idx].lsb)

        # Multiple fieldsets
        r = Register()
        r.size = 64
        etree = ET.parse(TEST_XML_MULTIPLE_FIELDSETS_PATH)
        reg_node = etree.getroot().find("./registers/register")
        self.parser._set_register_fields(r, reg_node)
        self.assertEqual(len(r.fieldsets), len(TEST_XML_MULTIPLE_FIELDSETS.fieldsets))
        for fs_idx, fs in enumerate(r.fieldsets):
            self.assertEqual(len(fs.fields), len(TEST_XML_MULTIPLE_FIELDSETS.fieldsets[fs_idx].fields))
            for f_idx, f in enumerate(fs.fields):
                self.assertEqual(f.name, TEST_XML_MULTIPLE_FIELDSETS.fieldsets[fs_idx].fields[f_idx].name)
                self.assertEqual(f.msb, TEST_XML_MULTIPLE_FIELDSETS.fieldsets[fs_idx].fields[f_idx].msb)
                self.assertEqual(f.lsb, TEST_XML_MULTIPLE_FIELDSETS.fieldsets[fs_idx].fields[f_idx].lsb)


        etree = ET.parse(TEST_XML_INVALID_FIELD_PATH)
        reg_node = etree.getroot().find("./registers/register")
        self.assertRaises(ShoulderParserException, self.parser._set_register_fields, r, reg_node)

    def test_parse_instructions(self):
        self.assertRaises(NotImplementedError, self.parser.parse_instructions, "")
