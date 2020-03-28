from pal.model.access_mechanism import AbstractAccessMechanism
from dataclasses import dataclass

@dataclass()
class Write(AbstractAccessMechanism):
    """ Generic access mechanism for writing a value """

    component: str = ""
    """ Name of the component that the register belongs to """

    offset: int = 0
    """ Register offset """

    name: str = "write"
    """ The name of this access mechanism  """

    def is_read(self):
        return False

    def is_write(self):
        return True

    def is_memory_mapped(self):
        return True

    def is_valid(self):
        return True
