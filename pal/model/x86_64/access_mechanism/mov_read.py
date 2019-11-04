from pal.model.access_mechanism import AbstractAccessMechanism
from dataclasses import dataclass

@dataclass()
class MOVRead(AbstractAccessMechanism):
    """ Access mechanism reading a value using the x86 MOV instruction """

    source_mnemonic: str = ""
    """ The source assembler mnemonic for the MOV instruction  """

    name: str = "mov_read"
    """ The name of this access mechanism  """

    def is_read(self):
        return True

    def is_write(self):
        return False

    def is_valid(self):
        # TODO: Check source assembler mnemonic is valid
        return True
