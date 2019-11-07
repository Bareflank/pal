from pal.model.access_mechanism import AbstractAccessMechanism
from dataclasses import dataclass

@dataclass()
class RDMSR(AbstractAccessMechanism):
    """ Access mechanism for reading a model specific register (MSR) """

    address: int = 0
    """ The address of the MSR to be read  """

    name: str = "rdmsr"
    """ The name of this access mechanism  """

    def is_read(self):
        return True

    def is_write(self):
        return False

    def is_memory_mapped(self):
        return False

    def is_valid(self):
        # TODO: Check within valid MSR address range
        return True
