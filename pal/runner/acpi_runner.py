import os
import copy

from pal.runner.abstract_runner import AbstractRunner
from pal.parser import parse_registers
from pal.parser import parse_instructions

class AcpiRunner(AbstractRunner):
    def run(self, generators):
        input_root = self.config.pal_data_dir
        output_root = self.config.pal_output_dir

        for generator in generators:
            acpi_top_dir = os.path.join(input_root, "acpi")
            acpi_sub_dirs = next(os.walk(acpi_top_dir))[1]
            for subdir in acpi_sub_dirs:
                indir = os.path.join(acpi_top_dir, subdir)
                outdir = os.path.join(output_root, "acpi", subdir)
                os.makedirs(outdir, exist_ok=True)
                regs = parse_registers(indir)
                generator.generate_registers(copy.deepcopy(regs), outdir)
