from pal.model.access_mechanism import AbstractAccessMechanism
from dataclasses import dataclass

@dataclass()
class CPUID(AbstractAccessMechanism):
    """ Access mechanism for reading information from the CPUID instruction """

    leaf: bytes = 0
    """ The CPUID leaf to be read (eax)  """

    output: str = "eax"
    """ The output register that CPUID reads information into  """
    """ Options: eax, ebx, ecx, edx  """

    name: str = "cpuid"
    """ The name of this access mechanism  """

    def is_read(self):
        return True

    def is_write(self):
        return False

    def is_valid(self):
        if str(output).lower() not in ["eax", "ebx", "ecx", "edx"]:
            return False

        # TODO: Check leaf/subleaf within valid range

        return True
