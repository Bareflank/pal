import sys
import os
import copy

from pal.cmd_args import parse_cmd_args
from pal.parser import parse_registers
from pal.writer.writer_factory import make_writer

from pal.generator.cxx_header_generator import CxxHeaderGenerator


def main_intel_x64(config, generator):

    data_path = config.pal_data_dir
    print("DATA PATH: " + data_path)

    indir = os.path.join(data_path, "x86_64/register/control_register")
    outdir = os.path.join(config.pal_output_dir, "control_register")
    os.makedirs(outdir, exist_ok=True)
    regs = parse_registers(indir)
    generator.generate(copy.deepcopy(regs), outdir)

    indir = os.path.join(data_path, "x86_64/register/cpuid")
    outdir = os.path.join(config.pal_output_dir, "cpuid")
    os.makedirs(outdir, exist_ok=True)
    regs = parse_registers(indir)
    generator.generate(copy.deepcopy(regs), outdir)

    indir = os.path.join(data_path, "x86_64/register/msr")
    outdir = os.path.join(config.pal_output_dir, "msr")
    os.makedirs(outdir, exist_ok=True)
    regs = parse_registers(indir)
    generator.generate(copy.deepcopy(regs), outdir)


def main_armv8a(config, generator):
    data_path = config.pal_data_dir

    indir = os.path.join(data_path, "armv8-a/register/aarch64")
    outdir = os.path.join(config.pal_output_dir, "aarch64")
    os.makedirs(outdir, exist_ok=True)
    regs = parse_registers(indir)
    generator.generate(copy.deepcopy(regs), outdir)

    indir = os.path.join(data_path, "armv8-a/register/aarch32")
    outdir = os.path.join(config.pal_output_dir, "aarch32")
    os.makedirs(outdir, exist_ok=True)
    regs = parse_registers(indir)
    generator.generate(copy.deepcopy(regs), outdir)

    indir = os.path.join(data_path, "armv8-a/register/external")
    outdir = os.path.join(config.pal_output_dir, "external")
    os.makedirs(outdir, exist_ok=True)
    regs = parse_registers(indir)
    generator.generate(copy.deepcopy(regs), outdir)


def pal_main():
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


pal_main()
