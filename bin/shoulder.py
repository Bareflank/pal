#!/usr/bin/env python3
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

print("Hello from the shoulder package!")

#  if __name == "__main__":
#      from shoulder.parser.armv8_xml_parser import ArmV8XmlParser
#      from shoulder.config import config
#      import glob
#
#      config.cxx_namespace = "aarch64"
#      parser = ArmV8XmlParser()
#      generator = CxxHeaderGenerator()
#      minified_generator = CxxMinifiedHeaderGenerator()
#
#      paths = glob.glob("/Users/jared-ais/workspace/thunderlane/ARM_ASL/mra_tools/v8.3/SysReg_v83A_xml-00bet5/*.xml")
#      regs = []
#      for path in paths:
#          results = parser.parse_registers(path)
#          if results:
#              regs.append(results[0])
#      generator.generate(regs, TEST_OUTFILE2)
