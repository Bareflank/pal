from dataclasses import dataclass, field as datafield


@dataclass
class RegisterOperand():
    """ Models a register (physical) operand that an instruction operates on"""

    name: str = ""
    """ The name of this logical operand """

    input: bool = False
    """ True if this register is used as an instruction input """

    output: bool = False
    """ True if this register is used as an instruction output """
