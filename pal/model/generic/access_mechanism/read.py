from pal.model.access_mechanism import AbstractAccessMechanism
from dataclasses import dataclass

@dataclass()
class Read(AbstractAccessMechanism):
    """ Generic access mechanism for reading a value """

    component: str = ""
    """ Name of the component that the register belongs to """

    offset: int = 0
    """ Register offset """

    name: str = "read"
    """ The name of this access mechanism  """

    def is_read(self):
        return True

    def is_write(self):
        return False

    def is_memory_mapped(self):
        return True

    def is_valid(self):
        return True
