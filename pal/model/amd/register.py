from dataclasses import dataclass, field as datafield
from typing import List, Dict

from pal.logger import logger
from pal.model.register import Register
from pal.model.fieldset import Fieldset
from pal.model.access_mechanism import AbstractAccessMechanism


@dataclass
class AmdRegister(Register):
    """ Models a register in the AMD x86_64 architecture """

    arch: str = "amd"

    access_mechanisms: Dict[str, List[AbstractAccessMechanism]] \
        = datafield(default_factory= lambda: {
            "mov_read": [],
            "mov_write": [],
            "read_pci_config": [],
            "write_pci_config": [],
            "cpuid": [],
            "rdmsr": [],
            "wrmsr": [],
        })
