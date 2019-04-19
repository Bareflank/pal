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

from shoulder.model.access_mechanism.abstract_access_mechanism import AbstractAccessMechanism
from dataclasses import dataclass

@dataclass(frozen=True)
class ReadCoprocessorRegister(AbstractAccessMechanism):
    """ Access mechanism for reading a system control coprocessor register """

    coproc: bytes
    """ Coprocessor number """

    opc1: bytes
    """ Coprocessor-specific opcode """

    opc2: bytes
    """ Optional coprocessor-specific opcode """

    crn: bytes
    """ Register number within the system control coprocessor """

    crm: bytes
    """ Operational register within CRn """

    operand_mnemonic: str
    """ The operand mnemonic of the register to be accessed """

    def instruction_mnemonic(self):
        return "MRC"

    def is_read(self):
        return True

    def is_write(self):
        return False

    def is_valid(self):
        raise NotImplementedError()

    def binary_encoded(self):
        raise NotImplementedError()
