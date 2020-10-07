from dataclasses import dataclass, field as datafield
from typing import List

from pal.model.logical_operand import LogicalOperand
from pal.model.register_operand import RegisterOperand

@dataclass
class ExecutionContext():
    """ Models the context under which an instruction may be executed """

    execution_state: str = ""
    """ The name of the execution state an instruction is executable in """

    logical_inputs: List[LogicalOperand] = datafield(default_factory= lambda: [])
    """ List of logical values this instruction takes as inputs """

    logical_ouputs: List[LogicalOperand] = datafield(default_factory= lambda: [])
    """ List of logical values this instruction produces as outputs """

    register_operands: List[RegisterOperand] = datafield(default_factory= lambda: [])
    """ List of registers this instruction operates on """
