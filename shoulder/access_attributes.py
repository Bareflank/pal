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

class AccessAttributes(object):
    def __init__(self):
        self.op0 = None
        self.op1 = None
        self.op2 = None
        self.crn = None
        self.crm = None
        self.mnemonic = None

    def __str__(self):
        msg = "{mnemonic}\n"
        msg += "op0: {op0}\n"
        msg += "op1: {op1}\n"
        msg += "op2: {op2}\n"
        msg += "CRn: {crn}\n"
        msg += "CRm: {crm}\n"
        msg = msg.format(**self.__dict__)

        msg += "Get Encoding:\n\t{bin_enc}\n\t{hex_enc}\n\t{dec_enc}\n"
        msg = msg.format(
            bin_enc = bin(self.sysreg_get_encoding()),
            hex_enc = hex(self.sysreg_get_encoding()),
            dec_enc = self.sysreg_get_encoding()
        )

        msg += "Set Encoding:\n\t{bin_enc}\n\t{hex_enc}\n\t{dec_enc}"
        msg = msg.format(
            bin_enc = bin(self.sysreg_set_encoding()),
            hex_enc = hex(self.sysreg_set_encoding()),
            dec_enc = self.sysreg_set_encoding()
        )

        return msg

    def is_valid(self):
        if self.op0 is None: return False
        if self.op1 is None: return False
        if self.op2 is None: return False
        if self.crn is None: return False
        if self.crm is None: return False
        if self.mnemonic is None: return False
        return True

    def sysreg_get_encoding(self):
        encoding = 0

        header = 0b1101010100
        l = 0b1
        return_reg = 0b00000

        encoding = encoding | (header << 22) | (l << 21) | (self.op0 << 19) |  \
                   (self.op1 << 16) | (self.crn << 12) | (self.crm << 8) |     \
                   (self.op2 << 5) | return_reg

        return encoding

    def sysreg_set_encoding(self):
        encoding = 0

        header = 0b1101010100
        l = 0b0
        value_reg = 0b00000

        encoding = encoding | (header << 22) | (l << 21) | (self.op0 << 19) |  \
                   (self.op1 << 16) | (self.crn << 12) | (self.crm << 8) |     \
                   (self.op2 << 5) | value_reg

        return encoding
