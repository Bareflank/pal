from dataclasses import dataclass, field as datafield
from typing import List, Dict

from pal.model.register import Register
from pal.model.access_mechanism import AbstractAccessMechanism


@dataclass
class GenericRegister(Register):
    """ Models a generic register that does not belong to a particular """
    """ microarchitecture """

    arch: str = "generic"

    access_mechanisms: Dict[str, List[AbstractAccessMechanism]] \
        = datafield(default_factory= lambda: {
            "read": [],
            "write": [],
            "read_pci_config": [],
            "write_pci_config": [],
        })
