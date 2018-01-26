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
import logging

from shoulder.logger import ShoulderLogger
from shoulder.logger import logger

class TestLogger(unittest.TestCase):

    def test_init_logger(self):
        self.assertIsNotNone(logger)
        self.assertIsNotNone(ShoulderLogger())
        self.assertIsNotNone(ShoulderLogger(color=True))
        self.assertIsNotNone(ShoulderLogger(level="debug"))

    def test__get_logger(self):
        self.assertIsNotNone(logger._get_logger())

    def test__set_colors(self):
        from shoulder.logger import _colorama_available
        prev_colorama_setting = _colorama_available
        _colorama_available = True

        logger._set_colors(True)
        self.assertIsNotNone(logger._debug_color)
        self.assertIsNotNone(logger._info_color)
        self.assertIsNotNone(logger._warning_color)
        self.assertIsNotNone(logger._error_color)
        self.assertIsNotNone(logger._reset_color)

        logger._set_colors(False)
        self.assertEqual(logger._debug_color, "")
        self.assertEqual(logger._info_color, "")
        self.assertEqual(logger._warning_color, "")
        self.assertEqual(logger._error_color, "")
        self.assertEqual(logger._reset_color, "")

        _colorama_available = prev_colorama_setting
        logger._set_colors(True)

    def test__log_level(self):
        self.assertIsNotNone(logger._log_level("debug"))
        self.assertIsNotNone(logger._log_level("info"))
        self.assertIsNotNone(logger._log_level("warn"))
        self.assertIsNotNone(logger._log_level("error"))
        self.assertRaises(ValueError, logger.set_log_level, "invalid_level")
        self.assertRaises(ValueError, logger.set_log_level, None)
        self.assertRaises(ValueError, logger.set_log_level, 42)
        self.assertRaises(ValueError, logger.set_log_level, True)

    def test_set_log_level(self):
        logger.set_log_level("debug")
        self.assertRaises(ValueError, logger.set_log_level, "invalid_level")

    def test_debug(self):
        logger.set_log_level("debug")
        logger.debug("test debug message")

    def test_info(self):
        logger.info("test info message")

    def test_warn(self):
        logger.warn("test warning message")

    def test_error(self):
        logger.error("test error message")
