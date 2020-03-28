import sys
import os
import copy

from pal.cmd_args import parse_cmd_args
from pal.parser import parse_registers
from pal.transform import transforms
from pal.writer.writer_factory import make_writer
from pal.logger import logger

from pal.generator.c_header_generator import CHeaderGenerator
from pal.generator.cxx_header_generator import CxxHeaderGenerator
from pal.generator.yaml_data_generator import YamlDataGenerator


def main_intel_x64(config, generator):

    data_path = config.pal_data_dir

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

    indir = os.path.join(data_path, "x86_64/register/vmcs")
    outdir = os.path.join(config.pal_output_dir, "vmcs")
    os.makedirs(outdir, exist_ok=True)
    regs = parse_registers(indir)
    generator.generate(copy.deepcopy(regs), outdir)


def main_armv8a(config, generator):
    data_path = config.pal_data_dir

    if config.access_mechanism == "gas_aarch64" \
       or config.access_mechanism == "test":
        indir = os.path.join(data_path, "armv8-a/register/aarch64")
        outdir = os.path.join(config.pal_output_dir, "aarch64")
        os.makedirs(outdir, exist_ok=True)

        regs = parse_registers(indir)

        # Quirk: VMPIDR_EL2  and VPIDR_EL2 have mrc and mcr defined as primary
        # access mechanisms (which aren't compilable with an aarch64 toolchain)
        regs = transforms["remove_coprocessor_am"].transform(regs)

        generator.generate(copy.deepcopy(regs), outdir)

    if config.access_mechanism == "gas_aarch32" \
       or config.access_mechanism == "test":
        indir = os.path.join(data_path, "armv8-a/register/aarch32")
        outdir = os.path.join(config.pal_output_dir, "aarch32")
        os.makedirs(outdir, exist_ok=True)
        regs = parse_registers(indir)
        generator.generate(copy.deepcopy(regs), outdir)

    if config.access_mechanism == "yaml":
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


def main_acpi(config, generator):
    data_path = config.pal_data_dir

    from pal.logger import logger
    acpi_top_dir = os.path.join(data_path, "acpi")
    acpi_sub_dirs = next(os.walk(acpi_top_dir))[1]
    for subdir in acpi_sub_dirs:
        indir = os.path.join(acpi_top_dir, subdir)
        outdir = os.path.join(config.pal_output_dir, "acpi", subdir)
        os.makedirs(outdir, exist_ok=True)
        regs = parse_registers(indir)
        generator.generate(copy.deepcopy(regs), outdir)


def pal_main():
    config = parse_cmd_args(sys.argv[1:])
    config.validate()
    logger.set_log_level(config.log_level)

    writer = make_writer(
        config.arch,
        config.language,
        config.access_mechanism,
        config.print_mechanism,
        config.file_format
    )

    if config.generator == "c++_header":
        generator = CxxHeaderGenerator(writer)
    elif config.generator == "c_header":
        generator = CHeaderGenerator(writer)
    elif config.generator == "yaml":
        generator = YamlDataGenerator(writer)
    else:
        raise Exception("Invalid generator: " + str(config.generator))

    if config.arch == "intel_x64":
        main_intel_x64(config, generator)
    elif config.arch == "armv8-a":
        main_armv8a(config, generator)
    else:
        raise Exception("Invalid architecture: " + str(config.arch))

    if config.acpi:
        main_acpi(config, generator)

pal_main()
