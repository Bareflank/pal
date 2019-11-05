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
from shoulder.model.fieldset import Fieldset
from shoulder.model.access_mechanism import AbstractAccessMechanism


@dataclass
class Register():
    """ Models a register """

    name: str = ""
    """ The abbreviated/symbolic/accronym name for this register """

    long_name: str = ""
    """ The non-abbreviated/spelled out name for this register """

    purpose: str = ""
    """ A description of this register's purpose """

    size: int = 64
    """ The size (in bits) of this register """

    arch: str = "none"
    """ The name of the architecture this register belongs to """

    is_internal: bool = False
    """ True if the register is internal to a CPU """

    is_optional: bool = False
    """ True if this register is an optional feature of the architecture """

    is_indexed: bool = False
    """ True if the register has many instances, accessable via an index """

    access_mechanisms: Dict[str, List[AbstractAccessMechanism]] \
        = datafield(default_factory= lambda: {})
    """ Access mechanisms by which this register is readable/writable """

    fieldsets: List[Fieldset] = datafield(default_factory= lambda: [])
    """ List of fieldsets that define all fields/bitfields in this register """

    def is_valid(self):
        for fs in self.fieldsets:
            if not fs.is_valid(): return False

        for am_list in self.access_mechanisms.values():
            for am in am_list:
                if not am.is_valid(): return False

        return True

    def is_readable(self):
        for am_list in self.access_mechanisms.values():
            for am in am_list:
                if am.is_read(): return True

        return False

    def is_writeable(self):
        for am_list in self.access_mechanisms.values():
            for am in am_list:
                if am.is_write(): return True

        return False
