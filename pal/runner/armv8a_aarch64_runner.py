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

        if self.config.language == "c" or self.config.language == "c++11":
            output_root = os.path.join(output_root, "include/pal")

        if self.config.language == "rust":
            output_root = os.path.join(output_root, "src")
            libfile = os.path.join(output_root, "lib.rs")
            if not os.path.exists(libfile):
                with open(libfile, 'w'): pass

        for generator in generators:
            indir = os.path.join(input_root, "armv8a/register/aarch64")
            outdir = os.path.join(output_root, "aarch64")
            os.makedirs(outdir, exist_ok=True)
            regs = parse_registers(indir)

            # Quirk: VMPIDR_EL2  and VPIDR_EL2 have mrc and mcr defined as primary
            # access mechanisms (which aren't compilable with an aarch64 toolchain)
            regs = transforms["remove_coprocessor_am"].transform(regs)

            generator.generate_registers(copy.deepcopy(regs), outdir)
