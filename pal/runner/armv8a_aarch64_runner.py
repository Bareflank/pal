import os
import copy

from pal.runner.abstract_runner import AbstractRunner
from pal.parser import parse_registers
from pal.parser import parse_instructions
from pal.transform import transforms

class Armv8aAarch64Runner(AbstractRunner):
    def run(self, generators):
        input_root = self.config.pal_data_dir
        output_root = self.config.pal_output_dir

        for generator in generators:
            indir = os.path.join(input_root, "armv8-a/register/aarch64")
            outdir = os.path.join(output_root, "aarch64")
            os.makedirs(outdir, exist_ok=True)
            regs = parse_registers(indir)

            # Quirk: VMPIDR_EL2  and VPIDR_EL2 have mrc and mcr defined as primary
            # access mechanisms (which aren't compilable with an aarch64 toolchain)
            regs = transforms["remove_coprocessor_am"].transform(regs)

            generator.generate_registers(copy.deepcopy(regs), outdir)
