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
class MRC(AbstractAccessMechanism):
    """ Access mechanism for reading a 32-bit coprocessor register """

    coproc: bytes = 0
    """ Coprocessor number """

    opc1: bytes = 0
    """ Coprocessor-specific opcode """

    opc2: bytes = 0
    """ Optional coprocessor-specific opcode """

    crn: bytes = 0
    """ Register number within the system control coprocessor """

    crm: bytes = 0
    """ Operational register within CRn """

    rd: bytes = 0b0
    """ Destination general purpose register (default = r0) """

    name: str = "mrc"
    """ The name of this access mechanism """

    def is_read(self):
        return True

    def is_write(self):
        return False

    def is_valid(self):
        if self.coproc > 0b1111: return False
        if self.opc1 > 0b111: return False
        if self.opc2 > 0b111: return False
        if self.crn > 0b1111: return False
        if self.crm > 0b1111: return False
        if self.rd > 0b1111: return False

        return True

    def binary_encoded(self):
        encoding = 0b0
        condition = 0b1110      # Execute always
        inst_class = 0b1110     # Coprocessor register transfer instruction
        l = 0b1                 # Direction of transfer (1 = read, 0 = write)

        encoding |= condition << 28
        encoding |= inst_class << 24
        encoding |= (self.opc1 & 0b111) << 21
        encoding |= l << 20
        encoding |= (self.crn & 0b1111) << 16
        encoding |= (self.rd & 0b1111) << 12
        encoding |= (self.coproc & 0b1111) << 8
        encoding |= (self.opc2 & 0b111) << 5
        encoding |= 1 << 4
        encoding |= (self.crm & 0b1111)

        return encoding

    def __str__(self):
        msg = super().__str__()
        msg += "\n"
        msg += "\tAssembler Mnemonic: {instruction} p{coproc}, #{opc1}, r{rd}, "
        msg += "c{crn}, c{crm}, #{opc2};\n"
        msg = msg.format(
            instruction="MRC",
            coproc=self.coproc,
            opc1=self.opc1,
            crn=self.crn,
            crm=self.crm,
            opc2=self.opc2,
            rd=self.rd
        )

        msg += "\tInstruction Encoding:\n"
        encoding = self.binary_encoded()
        table =  "\t|-----------|-----------|--------|--|-----------|-----------|-----------|--------|--|----------|\n"
        table += "\t|   cond    |           |  opc1  |L |    crn    |    rd     |  coproc   |  opc2  |  |   crm    |\n"
        table += "\t|31 30 29 28|27 26 25 24|23 22 21|20|19 18 17 16|15 14 13 12|11 10 9  8 |7  6  5 |4 |3  2  1  0|\n"
        table += "\t|-----------|-----------|--------|--|-----------|-----------|-----------|--------|--|----------|\n"
        table += "\t|"
        for i in range(0, 32):
            table += str((encoding >> 31 - i) & 0b1)
            if i in [3, 7, 10, 11, 15, 19, 23, 26, 27]:
               table += " |";
            elif i == 31:
               table += "|";
            else:
               table += "  ";
        table += "\n"
        table +=  "\t|-----------|-----------|--------|--|-----------|-----------|-----------|--------|--|----------|\n"

        msg += table
        return msg
