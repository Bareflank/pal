from pal.model.access_mechanism import AbstractAccessMechanism
from dataclasses import dataclass

@dataclass()
class XGETBV(AbstractAccessMechanism):
    """ Access mechanism reading an extended control register using the """
    """ x86 XGETBV instruction """

    register: int = 0
    """ The register number to be read """

    name: str = "xgetbv"
    """ The name of this access mechanism  """

    def is_read(self):
        return True

    def is_write(self):
        return False

    def is_memory_mapped(self):
        return False

    def is_valid(self):
        return True
