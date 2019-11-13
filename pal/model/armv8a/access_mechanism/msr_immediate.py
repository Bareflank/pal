from pal.model.access_mechanism import AbstractAccessMechanism
from dataclasses import dataclass

@dataclass()
class MSRImmediate(AbstractAccessMechanism):
    """ Access mechanism for writing an immediate value to a system register """

    crn: bytes = 0
    """ ? """

    op0: bytes = 0
    """ ? """

    op1: bytes = 0
    """ ? """

    op2: bytes = 0
    """ ? """

    operand_mnemonic: str = ""
    """ The operand mnemonic of the register to be accessed """

    name: str = "msr_immediate"
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
