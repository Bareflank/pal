from pal.model.access_mechanism import AbstractAccessMechanism
from dataclasses import dataclass

@dataclass()
class WRMSR(AbstractAccessMechanism):
    """ Access mechanism for writing a model specific register (MSR) """

    address: int = 0
    """ The address of the MSR to be written  """

    name: str = "wrmsr"
    """ The name of this access mechanism  """

    def is_read(self):
        return False

    def is_write(self):
        return True

    def is_valid(self):
        # TODO: Check within valid MSR address range
        return True
