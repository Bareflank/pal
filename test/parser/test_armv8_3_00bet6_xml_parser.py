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

from shoulder.parser.armv8_3_00bet6_xml_parser import ArmV8_3_00bet6_XmlParser
from test.parser.test_armv8_xml_parser import TestArmV8XmlParser
from shoulder.logger import logger
from shoulder.config import config

class TestArmV8_3_00bet6_XmlParser(TestArmV8XmlParser):

    @classmethod
    def setUpClass(cls):
        cls.parser = ArmV8_3_00bet6_XmlParser()
        logger.set_log_level("silent")

    @classmethod
    def tearDownClass(cls):
        logger.set_log_level(config.log_level)

    def test_parser_init(self):
        self.assertIsNotNone(self.parser)

    def test_parser_properties(self):
        self.assertEqual(self.parser.aarch_version_major, 8)
        self.assertEqual(self.parser.aarch_version_minor, 3)
