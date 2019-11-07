from pal.model.access_mechanism import AbstractAccessMechanism
from dataclasses import dataclass

@dataclass()
class MRSBanked(AbstractAccessMechanism):
    """ Access mechanism for reading a banked system register """

    m: bytes = 0
    """ ? """

    r: bytes = 0
    """ ? """

    m1: bytes = 0
    """ ? """

    operand_mnemonic: str = ""
    """ The operand mnemonic of the register to be accessed """

    name: str = "mrs_banked"
    """ The name of this access mechanism """

    def is_read(self):
        return True

    def is_write(self):
        return False

    def is_memory_mapped(self):
        return False

    def is_valid(self):
        raise NotImplementedError()

    def binary_encoded(self):
        raise NotImplementedError()
