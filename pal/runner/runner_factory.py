from pal.runner.acpi_runner import AcpiRunner
from pal.runner.armv8a_aarch32_runner import Armv8aAarch32Runner
from pal.runner.armv8a_aarch64_runner import Armv8aAarch64Runner
from pal.runner.armv8a_external_runner import Armv8aExternalRunner
from pal.runner.intel_64bit_runner import Intel64bitRunner
from pal.runner.pcie_runner import PcieRunner
from pal.runner.yaml_runner import YamlRunner


def make_runners(config):
    runners = []

    if config.execution_state == "armv8a_aarch32":
        runners.append(Armv8aAarch32Runner(config))
        runners.append(Armv8aExternalRunner(config))

    if config.execution_state == "armv8a_aarch64":
        runners.append(Armv8aAarch64Runner(config))
        #  runners.append(Armv8aExternalRunner(config))

    if config.execution_state == "intel_64bit":
        runners.append(Intel64bitRunner(config))

    if config.acpi:
        runners.append(AcpiRunner(config))

    if config.pcie:
        runners.append(PcieRunner(config))

    if config.language == "yaml":
        runners.append(YamlRunner(config))

    return runners
