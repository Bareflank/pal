from pal.model.access_mechanism import AbstractAccessMechanism
from dataclasses import dataclass

@dataclass()
class LDR(AbstractAccessMechanism):
    """ Access mechanism for reading a system control coprocessor register """

    component: str = ""
    """ Name of the component that the register belongs to """

    offset: int = 0
    """ Register offset """

    name: str = "ldr"
    """ The name of this access mechanism """

    def is_read(self):
        return True

    def is_write(self):
        return False

    def is_memory_mapped(self):
        return True

    def is_valid(self):
        raise NotImplementedError()

    def binary_encoded(self):
        raise NotImplementedError()
