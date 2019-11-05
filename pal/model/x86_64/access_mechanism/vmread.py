from pal.model.access_mechanism import AbstractAccessMechanism
from dataclasses import dataclass

@dataclass()
class VMRead(AbstractAccessMechanism):
    """
    Access mechanism reading a value from a VMCS using the x86 vmread
    instruction
    """

    address: int = 0
    """ The address of the VMCS field to be read """

    name: str = "vmread"
    """ The name of this access mechanism  """

    def is_read(self):
        return True

    def is_write(self):
        return False

    def is_valid(self):
        # TODO
        return True

