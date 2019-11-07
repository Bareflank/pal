from pal.model.access_mechanism import AbstractAccessMechanism
from dataclasses import dataclass

@dataclass()
class VMSR(AbstractAccessMechanism):
    """ Access mechanism for writing a system vector control register """

    reg: bytes = 0
    """ ? """

    operand_mnemonic: str = ""
    """ The operand mnemonic of the register to be accessed """

    name: str = "vmsr"
    """ The name of this access mechanism """

    def is_read(self):
        return False

    def is_write(self):
        return True

    def is_memory_mapped(self):
        return False

    def is_valid(self):
        raise NotImplementedError()

    def binary_encoded(self):
        raise NotImplementedError()
