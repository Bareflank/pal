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
import sys

from shoulder.config import Configuration
from shoulder.config import ShoulderConfig
from test.support.constants import *

class TestConfiguration(unittest.TestCase):

    def test_configuration_init(self):
        c = Configuration("test_name", "test_val")
        self.assertIsNotNone(c)
        self.assertEqual(c.name, "test_name")
        self.assertIsNotNone(c.default_value, "test_val")

    def test_configuration_str(self):
        c = Configuration("test_name", "test_val")
        self.assertTrue(str(c))
        c.options = ["test_val", "test_val2"]
        self.assertTrue(str(c))

    def test_configuration_help(self):
        with open(os.devnull, 'w') as outfile:
            stdout = sys.stdout
            stderr = sys.stderr
            sys.stdout = outfile
            sys.stderr = outfile
            c = Configuration("test_name", "test_val")
            c.help()
            c.options = ["test_val", "test_val2"]
            c.help()
            sys.stdout = stdout
            sys.stderr = stderr

    def test_configuration_validate(self):
        c = Configuration("test_name", "test_val")
        c.validate()

        c.name = None
        self.assertRaises(AttributeError, c.validate)
        c.name = "test_name"

        c.description = None
        self.assertRaises(AttributeError, c.validate)
        c.description = "Description N/A"

        c.options = ["test_option_1", "test_option_2"]
        self.assertRaises(AttributeError, c.validate)

        c.options.append("test_val")
        c.validate()


class TestShoulderConfig(unittest.TestCase):

    def test_shoulderconfig_init(self):
        self.assertIsNotNone(ShoulderConfig())

    def test_shoulderconfig_str(self):
        sc = ShoulderConfig()
        sc.add_configuration(Configuration("test_name", "test_value"))
        self.assertTrue(str(sc))

    def test_shoulderconfig_getitem(self):
        sc = ShoulderConfig()
        sc.add_configuration(Configuration("test_name", "test_value"))
        value = sc["test_name"]
        self.assertEqual(value, "test_value")

        try:
            sc["does_not_exist"]
        except KeyError as e:
            self.assertTrue(e)

    def test_shoulderconfig_getattr(self):
        sc = ShoulderConfig()
        sc.add_configuration(Configuration("test_name", "test_value"))
        value = sc.test_name
        self.assertEqual(value, "test_value")

        try:
            sc.does_not_exist
        except AttributeError as e:
            self.assertTrue(e)

    def test_shoulderconfig_help(self):
        with open(os.devnull, 'w') as outfile:
            stdout = sys.stdout
            stderr = sys.stderr
            sys.stdout = outfile
            sys.stderr = outfile
            sc = ShoulderConfig()
            sc.help()
            c = Configuration("test_name", "test_val")
            sc.help()
            sys.stdout = stdout
            sys.stderr = stderr

    def test_shoulderconfig_add_configuration(self):
        sc = ShoulderConfig()

        sc.add_configuration(Configuration("test_name", "test_value"))
        self.assertTrue(sc._configurations)
        self.assertTrue(sc._configurations["test_name"].name == "test_name")
        self.assertTrue(sc._configurations["test_name"].value == "test_value")

        sc.add_configuration(Configuration("test_name2", "test_value2"))
        self.assertTrue(sc._configurations["test_name"].name == "test_name")
        self.assertTrue(sc._configurations["test_name"].value == "test_value")
        self.assertTrue(sc._configurations["test_name2"].name == "test_name2")
        self.assertTrue(sc._configurations["test_name2"].value == "test_value2")

        invalid_config = Configuration(None, None)
        self.assertRaises(AttributeError, sc.add_configuration, invalid_config)

    def test_shoulderconfig_validate(self):
        sc = ShoulderConfig()

        sc.add_configuration(Configuration("test_name", "test_value"))
        sc.validate()

        config = Configuration("test_name2", "test_value2")
        config.options = ["test_value2"]
        sc.add_configuration(config)
        sc.validate()

        sc.test_name2 = "val1"
        self.assertRaises(AttributeError, sc.validate)

        sc["test_name2"] = "test_value2"
        sc.validate()
