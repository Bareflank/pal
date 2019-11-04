from pal.config import config
import logging
try:
    import colorama
    colorama.init()
    _colorama_available = True
except Exception as e:
    _colorama_available = False

class PalLogger:
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
        logger = logging.getLogger("pal_logger")
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
        debug_msg += "[PAL_DEBUG] " + msg
        debug_msg += self._reset_color
        self.logger.debug(debug_msg)

    def info(self, msg):
        """ Log a message about normal program operation """
        info_msg = self._info_color
        info_msg += "[PAL_INFO] " + msg
        info_msg += self._reset_color
        self.logger.info(info_msg)

    def warn(self, msg):
        """ Log an indication that something unexpected has happened """
        warning_msg = self._warning_color
        warning_msg += "[PAL_WARNING] " + msg
        warning_msg += self._reset_color
        self.logger.warning(warning_msg)

    def error(self, msg):
        """ Log an error message """
        error_msg = self._error_color
        error_msg += "[PAL_ERROR] " + msg
        error_msg += self._reset_color
        self.logger.error(error_msg)

# -----------------------------------------------------------------------------
# Module interface
# -----------------------------------------------------------------------------
#
# Usage:
#
# from pal.logger import logger
# logger.info("An info message")

logger = PalLogger(color=config.log_with_color, level=config.log_level)
