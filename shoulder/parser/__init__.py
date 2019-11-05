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
from shoulder.exception import ShoulderParserException
from shoulder.parser.armv8_xml_parser import ArmV8XmlParser
from shoulder.parser.bfmsr_parser import BfMsrParser
from shoulder.parser.shoulder_model_parser import ShoulderModelParser

# -----------------------------------------------------------------------------
# Module interface
# -----------------------------------------------------------------------------

# Usage:
#
# from shoulder.parser import parse_registers
# regs = parse_registers("<path/to/xml/spec/register.xml>")


def parse_registers(spec_path):
    if not os.path.exists(spec_path):
        msg = "Failed to parse registers, spec not found at: " + str(spec_path)
        logger.error(msg)
        raise ShoulderParserException(msg)

    logger.info("Parsing registers from: " + str(spec_path))

    regs = []

    #  paths = glob.glob(spec_path + "/*.xml")
    #  parser = ArmV8XmlParser()

    paths = glob.glob(spec_path + "/*.yml")
    parser = ShoulderModelParser()

    for path in paths:
        results = parser.parse_file(path)
        if results:
            for result in results:
                regs.append(result)

    logger.debug("Registers parsed: " + str(len(regs)))
    return regs
