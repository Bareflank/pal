import os
import copy

from pal.runner.abstract_runner import AbstractRunner
from pal.parser import parse_registers
from pal.parser import parse_instructions

class YamlRunner(AbstractRunner):
    def run(self, generators):
        input_root = self.config.pal_data_dir
        output_root = self.config.pal_output_dir
        output_root = os.path.join(output_root, "data")

        for generator in generators:
            indir = os.path.join(input_root, "armv8a/register/aarch64")
            outdir = os.path.join(ouput_root, "armv8a/register/aarch64")
            os.makedirs(outdir, exist_ok=True)
            regs = parse_registers(indir)
            generator.generate_registers(copy.deepcopy(regs), outdir)

            indir = os.path.join(input_root, "armv8a/register/aarch32")
            outdir = os.path.join(ouput_root, "armv8a/register/aarch32")
            os.makedirs(outdir, exist_ok=True)
            regs = parse_registers(indir)
            generator.generate_registers(copy.deepcopy(regs), outdir)
