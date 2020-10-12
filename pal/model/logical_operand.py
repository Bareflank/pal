from dataclasses import dataclass, field as datafield


@dataclass
class LogicalOperand():
    """ Models a logical (software) operand that an instruction operates on"""

    name: str = ""
    """ The name of this logical operand """

    type: str = ""
    """
    The type of this logical operand:
        int8, int16, int32, int64, uint8, uint16, uint32, uint64, bool
    """
