from pal.model.access_mechanism import AbstractAccessMechanism
from dataclasses import dataclass

@dataclass()
class CPUID(AbstractAccessMechanism):
    """ Access mechanism for reading information from the CPUID instruction """

    function: bytes = 0
    """ The CPUID function to be read (eax)  """

    output: str = "eax"
    """ The output register that CPUID reads information into  """
    """ Options: eax, ebx, ecx, edx  """

    name: str = "cpuid"
    """ The name of this access mechanism  """

    def is_read(self):
        return True

    def is_write(self):
        return False

    def is_memory_mapped(self):
        return False

    def is_valid(self):
        if str(output).lower() not in ["eax", "ebx", "ecx", "edx"]:
            return False

        return True
