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
import glob

from shoulder.logger import logger
from shoulder.config import config
from shoulder.exception import *
from shoulder.parser.armv8_xml_parser import ArmV8XmlParser

# -----------------------------------------------------------------------------
# Module interface
# -----------------------------------------------------------------------------

# Usage:
#
# from shoulder.parser import *
# regs = parse_registers("<path/to/xml/spec/registers>")

def parse_registers(spec_path):
    if not os.path.exists(spec_path):
        msg = "Failed to parse registers, spec not found at: " + str(spec_path)
        logger.error(msg)
        raise ShoulderParserException(msg)

    logger.info("Parsing registers from: " + str(spec_path))

    paths = glob.glob(spec_path + "/*.xml")
    regs = []
    parser = ArmV8XmlParser()

    for path in paths:
        results = parser.parse_registers(path)
        if results:
            for result in results:
                regs.append(result)

    return regs
