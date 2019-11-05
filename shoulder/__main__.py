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

import sys
import os
import copy

from shoulder.cmd_args import parse_cmd_args
from shoulder.parser import parse_registers
from shoulder.writer.writer_factory import make_writer

from shoulder.generator.cxx_header_generator import CxxHeaderGenerator


def main_intel_x64(config, generator):

    data_path = config.shoulder_data_dir
    print("DATA PATH: " + data_path)

    indir = os.path.join(data_path, "x86_64/register/control_register")
    outdir = os.path.join(config.shoulder_output_dir, "control_register")
    os.makedirs(outdir, exist_ok=True)
    regs = parse_registers(indir)
    generator.generate(copy.deepcopy(regs), outdir)

    indir = os.path.join(data_path, "x86_64/register/cpuid")
    outdir = os.path.join(config.shoulder_output_dir, "cpuid")
    os.makedirs(outdir, exist_ok=True)
    regs = parse_registers(indir)
    generator.generate(copy.deepcopy(regs), outdir)

    indir = os.path.join(data_path, "x86_64/register/msr")
    outdir = os.path.join(config.shoulder_output_dir, "msr")
    os.makedirs(outdir, exist_ok=True)
    regs = parse_registers(indir)
    generator.generate(copy.deepcopy(regs), outdir)


def main_armv8a(config, generator):
    data_path = config.shoulder_data_dir

    indir = os.path.join(data_path, "armv8-a/register/aarch64")
    outdir = os.path.join(config.shoulder_output_dir, "aarch64")
    os.makedirs(outdir, exist_ok=True)
    regs = parse_registers(indir)
    generator.generate(copy.deepcopy(regs), outdir)

    indir = os.path.join(data_path, "armv8-a/register/aarch32")
    outdir = os.path.join(config.shoulder_output_dir, "aarch32")
    os.makedirs(outdir, exist_ok=True)
    regs = parse_registers(indir)
    generator.generate(copy.deepcopy(regs), outdir)

    indir = os.path.join(data_path, "armv8-a/register/external")
    outdir = os.path.join(config.shoulder_output_dir, "external")
    os.makedirs(outdir, exist_ok=True)
    regs = parse_registers(indir)
    generator.generate(copy.deepcopy(regs), outdir)


def shoulder_main():
    config = parse_cmd_args(sys.argv[1:])

    writer = make_writer(
        config.arch,
        config.language,
        config.access_mechanism,
        config.print_style,
        config.file_format
    )

    if config.generator == "c++_header":
        generator = CxxHeaderGenerator(writer)
    else:
        raise Exception("Invalid generator: " + str(config.generator))

    if config.arch == "intel_x64":
        main_intel_x64(config, generator)
    elif config.arch == "armv8-a":
        main_armv8a(config, generator)
    else:
        raise Exception("Invalid architecture: " + str(config.arch))


shoulder_main()
