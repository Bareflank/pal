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

from shoulder.model.access_mechanism import AbstractAccessMechanism
from dataclasses import dataclass

@dataclass()
class MSRImmediate(AbstractAccessMechanism):
    """ Access mechanism for writing an immediate value to a system register """

    crn: bytes = 0
    """ ? """

    op0: bytes = 0
    """ ? """

    op1: bytes = 0
    """ ? """

    op2: bytes = 0
    """ ? """

    operand_mnemonic: str = ""
    """ The operand mnemonic of the register to be accessed """

    name: str = "msr_immediate"
    """ The name of this access mechanism """

    def is_read(self):
        return False

    def is_write(self):
        return True

    def is_valid(self):
        raise NotImplementedError()

    def binary_encoded(self):
        raise NotImplementedError()
