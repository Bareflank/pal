import os
import copy

from pal.runner.abstract_runner import AbstractRunner
from pal.parser import parse_registers
from pal.parser import parse_instructions
from pal.validator import check_intel_access_mechanisms_group
from pal.validator import check_intel_cpuid_access_mechanisms_group
from pal.validator import check_intel_msr_name_long_name_group

class Intel64bitRunner(AbstractRunner):
    def run(self, generators):
        input_root = self.config.pal_data_dir
        output_root = self.config.pal_output_dir

        for generator in generators:

            indir = os.path.join(input_root, "x86_64/register/control_register")
            outdir = os.path.join(output_root, "control_register")
            os.makedirs(outdir, exist_ok=True)
            regs = parse_registers(indir)
            check_intel_access_mechanisms_group(regs)
            generator.generate_registers(copy.deepcopy(regs), outdir)

            indir = os.path.join(input_root, "x86_64/register/cpuid")
            outdir = os.path.join(output_root, "cpuid")
            os.makedirs(outdir, exist_ok=True)
            regs = parse_registers(indir)
            check_intel_cpuid_access_mechanisms_group(regs)
            generator.generate_registers(copy.deepcopy(regs), outdir)

            indir = os.path.join(input_root, "x86_64/register/msr")
            outdir = os.path.join(output_root, "msr")
            os.makedirs(outdir, exist_ok=True)
            regs = parse_registers(indir)
            check_intel_msr_name_long_name_group(regs)
            generator.generate_registers(copy.deepcopy(regs), outdir)

            indir = os.path.join(input_root, "x86_64/register/vmcs")
            outdir = os.path.join(output_root, "vmcs")
            os.makedirs(outdir, exist_ok=True)
            regs = parse_registers(indir)
            generator.generate_registers(copy.deepcopy(regs), outdir)

            indir = os.path.join(input_root, "x86_64/instruction/architectural")
            outdir = os.path.join(output_root, "instruction")
            os.makedirs(outdir, exist_ok=True)
            instructions = parse_instructions(indir)
            generator.generate_instructions(copy.deepcopy(instructions), outdir)

            indir = os.path.join(input_root, "x86_64/instruction/logical")
            outdir = os.path.join(output_root, "instruction")
            os.makedirs(outdir, exist_ok=True)
            instructions = parse_instructions(indir)
            generator.generate_instructions(copy.deepcopy(instructions), outdir)
