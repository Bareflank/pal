from dataclasses import dataclass, field as datafield
from typing import List, Dict

from pal.model.execution_context import ExecutionContext

@dataclass
class Instruction():
    """ Models an instruction """

    name: str = ""
    """ The abbreviated/symbolic/accronym name for this instruction """

    long_name: str = ""
    """ The non-abbreviated/spelled out name for this instruction """

    purpose: str = ""
    """ A description of this instruction's purpose """

    execution_contexts: List[ExecutionContext] = datafield(default_factory= lambda: [])
    """ List of execution contexts that define the usage of this instruction """
