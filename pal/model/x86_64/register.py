from dataclasses import dataclass, field as datafield
from typing import List, Dict

from pal.logger import logger
from pal.model.register import Register
from pal.model.fieldset import Fieldset
from pal.model.access_mechanism import AbstractAccessMechanism


@dataclass
class x86_64Register(Register):
    """ Models a register in the Intel x86_64 architecture """

    arch: str = "x86_64"

    execution_states: Dict[str, bool] \
        = datafield(default_factory= lambda: {
            "real_mode": False,
            "protected_mode": False,
            "64bit_mode": False,
            "compatibility_mode": False,
            "virtual_8086": False,
        })

    arch_variants: Dict[str, bool] \
        = datafield(default_factory= lambda: {
            "skylake": False,
            "goldmont": False,
            "kaby_lake": False,
            "coffee_lake": False,
            "goldmont_plus": False,
            "cannon_lake": False,
            "whiskey_lake": False,
            "amber_lake": False,
            "cascade_lake": False,
            "comet_lake": False,
            "ice_lake": False,
        })

    access_mechanisms: Dict[str, List[AbstractAccessMechanism]] \
        = datafield(default_factory= lambda: {
            "mov_read": [],
            "mov_write": [],
            "cpuid": [],
            "rdmsr": [],
            "wrmsr": [],
            "vmread": [],
            "vmwrite": [],
        })
