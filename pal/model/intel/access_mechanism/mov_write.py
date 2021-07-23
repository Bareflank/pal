from pal.model.access_mechanism import AbstractAccessMechanism
from dataclasses import dataclass

@dataclass()
class MOVWrite(AbstractAccessMechanism):
    """ Access mechanism writing a value using the x86 MOV instruction """

    destination_mnemonic: str = ""
    """ The destination assembler mnemonic for the MOV instruction  """

    name: str = "mov_write"
    """ The name of this access mechanism  """

    def is_read(self):
        return False

    def is_write(self):
        return True

    def is_memory_mapped(self):
        return False

    def is_valid(self):
        # TODO: Check destination assembler mnemonic is valid
        return True
