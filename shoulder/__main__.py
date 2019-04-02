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

from shoulder.config import config
from shoulder.logger import logger
from shoulder.parser import *
from shoulder.generator import *
from shoulder.filter import filters

regs = parse_registers(config.xml_register_dir)
logger.debug("Registers parsed: " + str(len(regs)))

regs = filters["activity_monitor"].filter_exclusive(regs)
regs = filters["deprecated"].filter_exclusive(regs)
regs = filters["gic"].filter_exclusive(regs)
regs = filters["loregion"].filter_exclusive(regs)
regs = filters["misc"].filter_exclusive(regs)
regs = filters["mpam"].filter_exclusive(regs)
regs = filters["scxtnum"].filter_exclusive(regs)
regs = filters["statistical_profiling"].filter_exclusive(regs)
regs = filters["sve"].filter_exclusive(regs)
regs = filters["trace"].filter_exclusive(regs)
regs = filters["invalid"].filter_exclusive(regs)
logger.debug("Registers remaining after filters: " + str(len(regs)))

generate_all(regs, config.shoulder_output_dir)
