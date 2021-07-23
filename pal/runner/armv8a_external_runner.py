import os
import copy

from pal.runner.abstract_runner import AbstractRunner
from pal.parser import parse_registers
from pal.parser import parse_instructions

class Armv8aExternalRunner(AbstractRunner):
    def run(self, generators):
        input_root = self.config.pal_data_dir
        output_root = self.config.pal_output_dir

        if self.config.language == "c" or self.config.language == "c++11":
            output_root = os.path.join(output_root, "include/pal")

        if self.config.language == "rust":
            output_root = os.path.join(output_root, "src")
            libfile = os.path.join(output_root, "lib.rs")
            if not os.path.exists(libfile):
                with open(libfile, 'w'): pass

        for generator in generators:
            indir = os.path.join(input_root, "armv8a/register/external")
            outdir = os.path.join(output_root, "external")
            os.makedirs(outdir, exist_ok=True)
            regs = parse_registers(indir)
            generator.generate_registers(copy.deepcopy(regs), outdir)
