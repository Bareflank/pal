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
config.c_prefix = "aarch64"

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



#  import os
#  import glob
#
#  from shoulder.parser.intel_json_parser import IntelJsonParser
#  from shoulder.generator.intel_generator import IntelGenerator
#  from shoulder.config import config
#  from shoulder.logger import logger
#
#  indir = "/Users/jared-ais/workspace/thunderlane/intel_registers/"
#  outdir = os.path.abspath(os.path.join(config.shoulder_output_dir, "bfintrinsics"))
#  if not os.path.exists(outdir):
#          os.makedirs(outdir)
#
#  parser = IntelJsonParser()
#  g = IntelGenerator()
#
#  config.license_template_path = os.path.join("/Users/jared-ais/workspace/thunderlane/shoulder/scripts", "bareflank_license.txt")
#
#  # Root entries
#  infile = os.path.join(indir, "root_entry.json")
#  config.cxx_namespace = "intel_x64::vtd"
#  g.ifdef_name = "VTD_ROOT_TABLE_ENTRY_H"
#  regs = parser.parse_registers(infile)
#  outfile = os.path.abspath(os.path.join(outdir, "root_table_entry.h"))
#  g.generate(regs, outfile)
#
#  # Extended root entries
#  infile = os.path.join(indir, "extended_root_entry.json")
#  config.cxx_namespace = "intel_x64::vtd"
#  g.ifdef_name = "VTD_EXTENDED_ROOT_TABLE_ENTRY_H"
#  regs = parser.parse_registers(infile)
#  outfile = os.path.abspath(os.path.join(outdir, "extended_root_table_entry.h"))
#  g.generate(regs, outfile)
#
#  # Context entries
#  infile = os.path.join(indir, "context_entry.json")
#  config.cxx_namespace = "intel_x64::vtd"
#  g.ifdef_name = "VTD_CONTEXT_TABLE_ENTRY_H"
#  regs = parser.parse_registers(infile)
#  outfile = os.path.abspath(os.path.join(outdir, "context_table_entry.h"))
#  g.generate(regs, outfile)
#
#  # Extended context entries
#  infile = os.path.join(indir, "extended_context_entry.json")
#  config.cxx_namespace = "intel_x64::vtd"
#  g.ifdef_name = "VTD_EXTENDED_CONTEXT_TABLE_ENTRY_H"
#  regs = parser.parse_registers(infile)
#  outfile = os.path.abspath(os.path.join(outdir, "extended_context_table_entry.h"))
#  g.generate(regs, outfile)
#
#  # PASID entries
#  infile = os.path.join(indir, "pasid_entry.json")
#  config.cxx_namespace = "intel_x64::vtd"
#  g.ifdef_name = "VTD_PASID_ENTRY_H"
#  regs = parser.parse_registers(infile)
#  outfile = os.path.abspath(os.path.join(outdir, "pasid_entry.h"))
#  g.generate(regs, outfile)
#
#  # PASID state entries
#  infile = os.path.join(indir, "pasid_state_entry.json")
#  config.cxx_namespace = "intel_x64::vtd"
#  g.ifdef_name = "VTD_PASID_STATE_ENTRY_H"
#  regs = parser.parse_registers(infile)
#  outfile = os.path.abspath(os.path.join(outdir, "pasid_state_entry.h"))
#  g.generate(regs, outfile)
#
#  # First level paging structures
#  infile = os.path.join(indir, "first_level_paging_entries.json")
#  config.cxx_namespace = "intel_x64::vtd::flpe"
#  g.ifdef_name = "VTD_FIRST_LEVEL_PAGING_ENTRY_H"
#  regs = parser.parse_registers(infile)
#  outfile = os.path.abspath(os.path.join(outdir, "first_level_paging_entry.h"))
#  g.generate(regs, outfile)
#
#  # Second level paging structures
#  infile = os.path.join(indir, "second_level_paging_entries.json")
#  config.cxx_namespace = "intel_x64::vtd::slpe"
#  g.ifdef_name = "VTD_SECOND_LEVEL_PAGING_ENTRY_H"
#  regs = parser.parse_registers(infile)
#  outfile = os.path.abspath(os.path.join(outdir, "second_level_paging_entry.h"))
#  g.generate(regs, outfile)
#
#  # Fault record
#  infile = os.path.join(indir, "fault_record.json")
#  config.cxx_namespace = "intel_x64::vtd"
#  g.ifdef_name = "VTD_FAULT_RECORD_H"
#  regs = parser.parse_registers(infile)
#  outfile = os.path.abspath(os.path.join(outdir, "fault_record.h"))
#  g.generate(regs, outfile)
#
#  # Interupt remapping table entries (IRTE)
#  infile = os.path.join(indir, "interrupt_remapping_table_entry.json")
#  config.cxx_namespace = "intel_x64::vtd"
#  g.ifdef_name = "VTD_INTERRUPT_REMAPPING_TABLE_ENTRY_H"
#  regs = parser.parse_registers(infile)
#  outfile = os.path.abspath(os.path.join(outdir, "interrupt_remapping_table_entry.h"))
#  g.generate(regs, outfile)
#
#  # Posted Interrupt Descriptor
#  infile = os.path.join(indir, "posted_interrupt_descriptor.json")
#  config.cxx_namespace = "intel_x64::vtd"
#  g.ifdef_name = "VTD_POSTED_INTERRUPT_DESCRIPTOR_H"
#  regs = parser.parse_registers(infile)
#  outfile = os.path.abspath(os.path.join(outdir, "posted_interrupt_descriptor.h"))
#  g.generate(regs, outfile)
#



# import os
# import glob
#
# from shoulder.parser.iommu_json_parser import IommuJsonParser
# from shoulder.generator.iommu_generator import IommuGenerator
# from shoulder.generator.iommu_generator_2 import IommuGenerator2
# from shoulder.config import config
# from shoulder.logger import logger
#
# indir = "/Users/jared-ais/workspace/thunderlane/intel_registers/"
# outdir = os.path.abspath(os.path.join(config.shoulder_output_dir, "iommu"))
# if not os.path.exists(outdir):
#         os.makedirs(outdir)
#
# parser = IommuJsonParser()
# g = IommuGenerator2()
#
# config.license_template_path = os.path.join("/Users/jared-ais/workspace/thunderlane/shoulder/scripts", "bareflank_license.txt")
#
# # Root entries
# infile = os.path.join(indir, "iommu_registers.json")
# config.cxx_namespace = "intel_x64::vtd::iommu"
# g.ifdef_name = "VTD_IOMMU_H"
# regs = parser.parse_registers(infile)
#
# outfile = os.path.abspath(os.path.join(outdir, "iommu_2.h"))
# g.generate(regs, outfile)

