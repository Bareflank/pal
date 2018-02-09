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

class Register(object):
    """ Models a register in the ARM architecture """
    def __init__(self):
        self.name = None
        self.long_name = None
        self.purpose = None
        self.size = None
        self.is_sysreg = True
        self.fieldsets = []

    def __str__(self):
        msg = "{name} ({long_name})\nPurpose: {purpose}\nSize: {size}"
        msg += "\nSystem Register: {is_sysreg}"
        msg = msg.format(**self.__dict__)

        for fieldset in self.fieldsets:
            msg += "\n" + str(fieldset)

        return msg

    def add_fieldset(self, fieldset):
        self.fieldsets.append(fieldset)

    def is_valid(self):
        if self.name is None: return False
        if self.long_name is None: return False
        if self.size is None: return False
        if self.purpose is None: return False
        for fs in self.fieldsets:
            if not fs.is_valid(): return False
        return True
