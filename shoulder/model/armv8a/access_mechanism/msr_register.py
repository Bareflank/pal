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
class MSRRegister(AbstractAccessMechanism):
    """ Access mechanism for writing a system register using the contents of """
    """ a general purpose register """

    op0: bytes
    """ Top-level encoding of the system instruction type  """

    op1: bytes
    """ The lowest exception level at which the access is possible """

    op2: bytes
    """ Sub-encoding for the system instruction type  """

    crn: bytes
    """ Register number """

    crm: bytes
    """ Sub-register number  """

    operand_mnemonic: str
    """ The operand mnemonic of the register to be accessed """

    rt: bytes = 0b0
    """ Source general purpose register (default = x0) """

    def is_read(self):
        return False

    def is_write(self):
        return True

    def is_valid(self):
        if self.op0 > 0b11: return False
        if self.op1 > 0b111: return False
        if self.op2 > 0b111: return False
        if self.crn > 0b1111: return False
        if self.crm > 0b1111: return False
        if self.rt > 0b11111: return False

        return True

    def binary_encoded(self):
        encoding = 0b0
        header = 0b1101010100   # System register transfer instruction
        l = 0b0                 # Direction of transfer (1 = read, 0 = write)

        encoding |= header << 22
        encoding |= l << 21
        encoding |= (self.op0 & 0b11) << 19
        encoding |= (self.op1 & 0b111) << 16
        encoding |= (self.crn & 0b1111) << 12
        encoding |= (self.crm & 0b1111) << 8
        encoding |= (self.op2 & 0b111) << 5
        encoding |= (self.rt & 0b11111)

        return encoding

    def __str__(self):
        msg = super().__str__()
        msg += "\n"
        msg += "\tAssembler Mnemonic: {instruction} {operand}, x{rt};\n"
        msg = msg.format(
            instruction="MSR",
            operand=self.operand_mnemonic,
            rt=self.rt
        )

        msg += "\tInstruction Encoding:\n"
        encoding = self.binary_encoded()
        table =  "\t|-----------------------------|--|-----|--------|-----------|-----------|--------|-------------|\n"
        table += "\t|              S3             |L | op0 |  op1   |    CRn    |    CRm    |  op2   |     Rt      |\n"
        table += "\t|31 30 29 28 27 26 25 24 23 22|21|20 19|18 17 16|15 14 13 12|11 10 9  8 |7  6  5 |4  3  2  1  0|\n"
        table += "\t|-----------------------------|--|-----|--------|-----------|-----------|--------|-------------|\n"
        table += "\t|"
        for i in range(0, 32):
            table += str((encoding >> 31 - i) & 0b1)
            if i in [9, 10, 12, 15, 19, 23, 26]:
               table += " |";
            elif i == 31:
               table += "|";
            else:
               table += "  ";
        table += "\n"
        table += "\t|-----------------------------|--|-----|--------|-----------|-----------|--------|-------------|\n"

        msg += table
        return msg
