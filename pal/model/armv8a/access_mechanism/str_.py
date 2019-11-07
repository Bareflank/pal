from pal.model.access_mechanism import AbstractAccessMechanism
from dataclasses import dataclass

@dataclass()
class STR(AbstractAccessMechanism):
    """ Access mechanism for writing a memory mapped register """

    component: str = ""
    """ Component that the register is mapped to """

    offset: int = 0
    """ Register offset from base address """

    name: str = "str"
    """ The name of this access mechanism """

    def is_read(self):
        return False

    def is_write(self):
        return True

    def is_memory_mapped(self):
        return True

    def is_valid(self):
        raise NotImplementedError()

    def binary_encoded(self):
        raise NotImplementedError()
