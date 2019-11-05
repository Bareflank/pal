#
# Shoulder
# Copyright (C) 2018 Assured Information Security, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from dataclasses import dataclass, field as datafield
from typing import List, Dict

from shoulder.logger import logger
from shoulder.model.register import Register
from shoulder.model.fieldset import Fieldset
from shoulder.model.access_mechanism import AbstractAccessMechanism


@dataclass
class ARMv8ARegister(Register):
    """ Models a register in the ARMv8-A architecture profile """

    execution_state: str = None
    """ The execution state this register belongs to: """
    """ None = no associated execution state (i.e. memory mapped) """
    """ aarch32 = ARM 32-bit execution state """
    """ aarch64 = ARM 64-bit execution state """

    is_banked: bool = False
    """ True if the register is banked (has copies per exception level) """

    arch: str = "armv8-a"

    access_mechanisms: Dict[str, List[AbstractAccessMechanism]] \
        = datafield(default_factory= lambda: {
            "mrc": [],
            "mcr": [],
            "mrrc": [],
            "mcrr": [],
            "ldr": [],
            "str": [],
            "msr": [],
            "mrs_register": [],
            "mrs_banked": [],
            "msr_register": [],
            "msr_banked": [],
            "msr_immediate": [],
            "vmsr": [],
            "vmrs": [],
        })
