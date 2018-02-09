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

from shoulder.config import config
import logging
try:
    import colorama
    colorama.init()
    _colorama_available = True
except Exception as e:
    _colorama_available = False

class ShoulderLogger:
    def __init__(self, color=True, level="info"):
        self.log_levels = {
            'debug': logging.DEBUG,
            'info': logging.INFO,
            'warn': logging.WARNING,
            'error': logging.ERROR,
            'silent': logging.CRITICAL
        }
        self.logger = self._get_logger()
        self.set_log_level(level)
        self._set_colors(color)

    def _get_logger(self):
        logger = logging.getLogger("shoulder_logger")
        if logger.hasHandlers():
            return logger

        formatter = logging.Formatter('%(message)s')

        handler = logging.StreamHandler()
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        return logger

    def _set_colors(self, enable_colors):
        if _colorama_available and enable_colors == True:
            self._debug_color = colorama.Fore.WHITE
            self._info_color = colorama.Fore.GREEN
            self._warning_color = colorama.Fore.YELLOW
            self._error_color = colorama.Fore.RED
            self._reset_color = colorama.Style.RESET_ALL
        else:
            self._debug_color = ""
            self._info_color = ""
            self._warning_color = ""
            self._error_color = ""
            self._reset_color = ""

    def _log_level(self, level):
        _level = self.log_levels.get(level, None)  # None if level not found
        if not _level:
            msg = "Invalid log level \'" + str(level) + "\' specified, "
            msg += "please use: "
            for k, v in self.log_levels.items():
                msg += k + ", "
            raise ValueError(msg)
        else:
            return _level

    def set_log_level(self, level):
        self.logger.setLevel(self._log_level(level))

    def debug(self, msg):
        """ Log a message of interest only when diagnosing problems """
        debug_msg = self._debug_color
        debug_msg += "[SHOULDER_DEBUG] " + msg
        debug_msg += self._reset_color
        self.logger.debug(debug_msg)

    def info(self, msg):
        """ Log a message about normal program operation """
        info_msg = self._info_color
        info_msg += "[SHOULDER_INFO] " + msg
        info_msg += self._reset_color
        self.logger.info(info_msg)

    def warn(self, msg):
        """ Log an indication that something unexpected has happened """
        warning_msg = self._warning_color
        warning_msg += "[SHOULDER_WARNING] " + msg
        warning_msg += self._reset_color
        self.logger.warning(warning_msg)

    def error(self, msg):
        """ Log an error message """
        error_msg = self._error_color
        error_msg += "[SHOULDER_ERROR] " + msg
        error_msg += self._reset_color
        self.logger.error(error_msg)

# -----------------------------------------------------------------------------
# Module interface
# -----------------------------------------------------------------------------
#
# Usage:
#
# from shoulder.logger import logger
# logger.info("An info message")

logger = ShoulderLogger(color=config.log_with_color, level=config.log_level)
