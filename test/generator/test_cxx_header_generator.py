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
import io

from shoulder.generator.cxx_header_generator import CxxHeaderGenerator
from shoulder.register import Register
from shoulder.logger import logger
from shoulder.config import config
from shoulder.exception import *
from test.support.constants import *

TEST_OUTFILE = os.path.abspath(os.path.join(TEST_TOP_DIR, "out/output.txt"))

class TestCxxHeaderGenerator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.generator = CxxHeaderGenerator()
        logger.set_log_level("silent")

    @classmethod
    def tearDownClass(cls):
        logger.set_log_level(config.log_level)

    def test_generator_init(self):
        self.assertIsNotNone(self.generator)

    def test_generate(self):
        self.assertRaises(ShoulderGeneratorException, self.generator.generate, None, None)
        self.assertRaises(ShoulderGeneratorException, self.generator.generate, None, "/an/invalid/path")
        self.assertRaises(ShoulderGeneratorException, self.generator.generate, None, os.devnull)
        self.assertRaises(ShoulderGeneratorException, self.generator.generate, "invalid", os.devnull)
        self.generator.generate([Register()], os.devnull)

    def test_generate_license(self):
        test_file = io.StringIO()
        self.generator._generate_license(test_file)

        expected_file_path = os.path.abspath(os.path.join(TEST_TOP_DIR, "support/mock_generated_files/license.h"))
        with open(expected_file_path, "r") as expected_file:
            self.assertTrue(expected_file.read() == test_file.getvalue())

        test_file.close()

    def test_generate_cxx_includes(self):
        test_file = io.StringIO()
        self.generator._generate_cxx_includes(test_file)

        expected_file = io.StringIO("#include <stdint>\n#include \"regs.h\"\n\n")
        self.assertTrue(expected_file.getvalue() == test_file.getvalue())

    def test_generate_include_guard_open(self):
        test_file = io.StringIO()
        self.generator._generate_include_guard_open(test_file)

        expected_file = io.StringIO("#ifndef SHOULDER_AARCH64_H\n#define SHOULDER_AARCH64_H\n\n")
        self.assertTrue(expected_file.getvalue() == test_file.getvalue())

    def test_generate_include_guard_close(self):
        test_file = io.StringIO()
        self.generator._generate_include_guard_close(test_file)

        expected_file = io.StringIO("#endif\n\n")
        self.assertTrue(expected_file.getvalue() == test_file.getvalue())

    def test_generate_namespace_open(self):
        old_namespace = config.cxx_namespace

        config.cxx_namespace = None
        test_file = io.StringIO()
        self.generator._generate_namespace_open(test_file)
        expected_file = io.StringIO("")
        self.assertTrue(expected_file.getvalue() == test_file.getvalue())

        config.cxx_namespace = ""
        test_file = io.StringIO()
        self.generator._generate_namespace_open(test_file)
        expected_file = io.StringIO("")
        self.assertTrue(expected_file.getvalue() == test_file.getvalue())

        config.cxx_namespace = "namespace1"
        test_file = io.StringIO()
        self.generator._generate_namespace_open(test_file)
        expected_file = io.StringIO("namespace namespace1\n{\n")
        self.assertTrue(expected_file.getvalue() == test_file.getvalue())

        config.cxx_namespace = "namespace1::namespace2::namespace3"
        test_file = io.StringIO()
        self.generator._generate_namespace_open(test_file)
        expected_file = io.StringIO()
        expected_file.write("namespace namespace1\n{\n")
        expected_file.write("namespace namespace2\n{\n")
        expected_file.write("namespace namespace3\n{\n")
        self.assertTrue(expected_file.getvalue() == test_file.getvalue())

        config.cxx_namespace = "namespace1::namespace2:namespace3"
        test_file = io.StringIO()
        self.generator._generate_namespace_open(test_file)
        expected_file = io.StringIO()
        expected_file.write("namespace namespace1\n{\n")
        expected_file.write("namespace namespace2:namespace3\n{\n")
        self.assertTrue(expected_file.getvalue() == test_file.getvalue())

        config.cxx_namespace = "!@#$%^&*();?><{}[]\"\'"
        test_file = io.StringIO()
        self.generator._generate_namespace_open(test_file)
        expected_file = io.StringIO()
        expected_file.write("namespace !@#$%^&*();?><{}[]\"\'\n{\n")
        self.assertTrue(expected_file.getvalue() == test_file.getvalue())

        config.cxx_namespace = old_namespace

    def test_generate_namespace_close(self):
        old_namespace = config.cxx_namespace

        config.cxx_namespace = None
        test_file = io.StringIO()
        self.generator._generate_namespace_close(test_file)
        expected_file = io.StringIO("")
        self.assertTrue(expected_file.getvalue() == test_file.getvalue())

        config.cxx_namespace = ""
        test_file = io.StringIO()
        self.generator._generate_namespace_close(test_file)
        expected_file = io.StringIO("")
        self.assertTrue(expected_file.getvalue() == test_file.getvalue())

        config.cxx_namespace = "namespace1"
        test_file = io.StringIO()
        self.generator._generate_namespace_close(test_file)
        expected_file = io.StringIO("}\n")
        self.assertTrue(expected_file.getvalue() == test_file.getvalue())

        config.cxx_namespace = "namespace1::namespace2::namespace3"
        test_file = io.StringIO()
        self.generator._generate_namespace_close(test_file)
        expected_file = io.StringIO("}\n}\n}\n")
        self.assertTrue(expected_file.getvalue() == test_file.getvalue())

        config.cxx_namespace = "namespace1::namespace2:namespace3"
        test_file = io.StringIO()
        self.generator._generate_namespace_close(test_file)
        expected_file = io.StringIO("}\n}\n")
        self.assertTrue(expected_file.getvalue() == test_file.getvalue())

        config.cxx_namespace = "!@#$%^&*();?><{}[]\"\'"
        test_file = io.StringIO()
        self.generator._generate_namespace_close(test_file)
        expected_file = io.StringIO("}\n")
        self.assertTrue(expected_file.getvalue() == test_file.getvalue())

        config.cxx_namespace = old_namespace

    def test_generate_generate_objects(self):
        outfile = io.StringIO()

        self.generator._generate_objects([], outfile)

        r1 = Register()
        regs = [r1]
        self.generator._generate_objects(regs, outfile)

        regs.append("invalid_object_type")
        self.assertRaises(ShoulderGeneratorException, self.generator._generate_objects, regs, outfile)

    # This test covers _generarate_register, _generate_fieldsets,
    # _generate_single_fieldset, generate_bitfield_accessors, and
    # _generate_field_accessors
    def test_generate_register(self):
        test_outfile = io.StringIO()
        self.generator._generate_register(TEST_XML_NO_FIELDS, test_outfile)
        expected_file_path = TEST_GENERATED_REG_NO_FIELDS_PATH
        with open(expected_file_path, "r") as expected_file:
            self.assertTrue(expected_file.read() == test_outfile.getvalue())

        test_outfile = io.StringIO()
        self.generator._generate_register(TEST_XML_REG64, test_outfile)
        expected_file_path = TEST_GENERATED_REG64_PATH
        with open(expected_file_path, "r") as expected_file:
            self.assertTrue(expected_file.read() == test_outfile.getvalue())

        test_outfile = io.StringIO()
        self.generator._generate_register(TEST_XML_MULTIPLE_FIELDSETS, test_outfile)
        expected_file_path = TEST_GENERATED_REG_MULTIPLE_FIELDSETS_PATH
        with open(expected_file_path, "r") as expected_file:
            self.assertTrue(expected_file.read() == test_outfile.getvalue())


    def test_increase_indent(self):
        self.generator._current_indent_level = 0
        self.generator._increase_indent()
        self.assertEqual(self.generator._current_indent_level, 1)

    def test_decrease_indent(self):
        self.generator._current_indent_level = 1
        self.generator._decrease_indent()
        self.assertEqual(self.generator._current_indent_level, 0)

        self.assertRaises(ShoulderGeneratorException, self.generator._decrease_indent)

    def test_indent_string(self):
        self.generator._current_indent_level = 0
        indent = self.generator._indent_string()
        self.assertEqual(indent, "")

        self.generator._current_indent_level = 1
        indent = self.generator._indent_string()
        self.assertEqual(indent, "\t")

        self.generator._current_indent_level = 5
        indent = self.generator._indent_string()
        self.assertEqual(indent, "\t\t\t\t\t")
