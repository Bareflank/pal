import os
import copy

from pal.runner.abstract_runner import AbstractRunner
from pal.parser import parse_registers
from pal.parser import parse_instructions

class Armv8aExternalRunner(AbstractRunner):
    def run(self, generators):
        input_root = self.config.pal_data_dir
        output_root = self.config.pal_output_dir

        for generator in generators:
            indir = os.path.join(input_root, "armv8-a/register/external")
            outdir = os.path.join(output_root, "external")
            os.makedirs(outdir, exist_ok=True)
            regs = parse_registers(indir)
            generator.generate_registers(copy.deepcopy(regs), outdir)
