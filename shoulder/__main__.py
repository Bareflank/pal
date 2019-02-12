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

from shoulder.parser.armv8_xml_parser import ArmV8XmlParser
from shoulder.generator.c_header_generator import CHeaderGenerator
from shoulder.generator.cxx_header_generator import CxxHeaderGenerator
from shoulder.config import config
from shoulder.logger import logger
from shoulder.filters import *

def printReg(reg):
    logger.info("NAME:\n    " + reg.name)
    logger.info("LONG NAME:\n    " + reg.long_name)
    logger.info("PURPOSE:\n    " + reg.purpose)
    logger.info("SIZE:\n    " + str(reg.size))
    logger.info("OFFSET:\n    " + str(reg.offset))
    logger.info("IS_SYSREG:\n    " + str(reg.is_sysreg))
    msg = ""
    for fieldset in reg.fieldsets:
        msg += "\n" + str(fieldset)
    logger.info("FIELDSETS:" + msg)


# SETUP
logger.set_log_level("info")
test_input_dir = "/home/jzepf/Projects/Scapula/ARM-SysReg-v85A-00bet9/SysReg_v85A_xml-00bet9/"
config.c_prefix = "aarch"

# PARSE
logger.info("Parsing registers from: " + str(test_input_dir))
paths = glob.glob(test_input_dir + "*.xml")
regs = []
parser = ArmV8XmlParser()
for path in paths:
    results = parser.parse_registers(path)
    if results:
        regs.append(results[0])

# FILTER
regs = apply_filters(regs)

# GENERATE
if not os.path.exists(config.shoulder_output_dir):
    os.makedirs(config.shoulder_output_dir)
c_generator = CHeaderGenerator()
c_generator.generate(regs, (config.shoulder_output_dir + "/c_shoulder.h"))

cxx_generator = CxxHeaderGenerator()
cxx_generator.generate(regs, (config.shoulder_output_dir + "/cxx_shoulder.h"))



#  import os
#  import glob
#
#  from shoulder.parser.armv8_xml_parser import ArmV8XmlParser
#  from shoulder.generator import *
#  from shoulder.config import config
#  from shoulder.logger import logger
#  from shoulder.filters import *
#
#  # TODO Import configuration from command line arguments
#  test_input_dir = "/Users/jared-ais/workspace/thunderlane/ARM_ASL/mra_tools/v8.3/SysReg_v83A_xml-00bet5/"
#  config.cxx_namespace = "aarch64"
#
#  # Parse all input registers
#  logger.info("Parsing registers from: " + str(test_input_dir))
#  paths = glob.glob(test_input_dir + "*.xml")
#  regs = []
#  parser = ArmV8XmlParser()
#  for path in paths:
#      results = parser.parse_registers(path)
#      if results:
#          regs.append(results[0])
#
#  # Apply filters (shoulder.filters.*)
#  regs = apply_filters(regs)
#
#  # Generate output files (shoulder.generator.*)
#  generate_all(regs, config.shoulder_output_dir)
