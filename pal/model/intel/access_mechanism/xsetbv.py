from pal.model.access_mechanism import AbstractAccessMechanism
from dataclasses import dataclass

@dataclass()
class XSETBV(AbstractAccessMechanism):
    """ Access mechanism writing to an extended control register using the """
    """ x86 XSETBV instruction """

    register: int = 0
    """ The register number to be read """

    name: str = "xsetbv"
    """ The name of this access mechanism  """

    def is_read(self):
        return False

    def is_write(self):
        return True

    def is_memory_mapped(self):
        return False

    def is_valid(self):
        return True
