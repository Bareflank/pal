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
class x86_64Register(Register):
    """ Models a register in the Intel x86_64 architecture """

    arch: str = "x86_64"

    execution_states: Dict[str, bool] \
        = datafield(default_factory= lambda: {
            "real_mode": False,
            "protected_mode": False,
            "64bit_mode": False,
            "compatibility_mode": False,
            "virtual_8086": False,
        })

    arch_variants: Dict[str, bool] \
        = datafield(default_factory= lambda: {
            "skylake": False,
            "goldmont": False,
            "kaby_lake": False,
            "coffee_lake": False,
            "goldmont_plus": False,
            "cannon_lake": False,
            "whiskey_lake": False,
            "amber_lake": False,
            "cascade_lake": False,
            "comet_lake": False,
            "ice_lake": False,
        })

    access_mechanisms: Dict[str, List[AbstractAccessMechanism]] \
        = datafield(default_factory= lambda: {
            "mov_read": [],
            "mov_write": [],
            "cpuid": [],
            "rdmsr": [],
            "wrmsr": [],
            "vmread": [],
            "vmwrite": [],
        })
