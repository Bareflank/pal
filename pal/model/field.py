from dataclasses import dataclass


@dataclass
class Field():
    """ Models a single named field (or bitfield) in a register fieldset """

    name: str = ""
    """ The abbreviated/symbolic/accronym name for this field """

    msb: int = 0
    """ Most significant bit that the field occupies within a register """

    lsb: int = 0
    """ Least significant bit that the field occupies within a register """

    long_name: str = ""
    """ The non-abbreviated/spelled out name for this field """

    description: str = ""
    """ A description of this field """

    readable: bool = False
    """ True if this field is readable  """

    writable: bool = False
    """ True if this field is writable  """

    lockable: bool = False
    """ True if this field can be locked  """

    write_once: bool = False
    """ True if this field becomes locked after writing to it once  """

    write_1_clear: bool = False
    """ True if this field is cleared (set to '0') by writing a '1' to it  """

    reserved0: bool = False
    """ True if the value of this field is reserved 0  """

    reserved1: bool = False
    """ True if the value of this field is reserved 1  """

    preserved: bool = False
    """ True if the value of this field should be preserved across writes  """
