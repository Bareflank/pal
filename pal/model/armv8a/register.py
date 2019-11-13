from dataclasses import dataclass, field as datafield
from typing import List, Dict

from pal.logger import logger
from pal.model.register import Register
from pal.model.fieldset import Fieldset
from pal.model.access_mechanism import AbstractAccessMechanism


@dataclass
class ARMv8ARegister(Register):
    """ Models a register in the ARMv8-A architecture profile """

    execution_state: str = None
    """ The execution state this register belongs to: """
    """ None = no associated execution state (i.e. memory mapped) """
    """ aarch32 = ARM 32-bit execution state """
    """ aarch64 = ARM 64-bit execution state """

    is_banked: bool = False
    """ True if the register is banked (has copies per exception level) """

    arch: str = "armv8-a"

    access_mechanisms: Dict[str, List[AbstractAccessMechanism]] \
        = datafield(default_factory= lambda: {
            "mrc": [],
            "mcr": [],
            "mrrc": [],
            "mcrr": [],
            "ldr": [],
            "str": [],
            "msr": [],
            "mrs_register": [],
            "mrs_banked": [],
            "msr_register": [],
            "msr_banked": [],
            "msr_immediate": [],
            "vmsr": [],
            "vmrs": [],
        })
