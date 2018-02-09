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

from collections import namedtuple

# Tuple for representing bit positions of a named bit field
Field = namedtuple('Field', 'name msb lsb')

class Fieldset(object):
    """ Models a collection of named fields that apply to a register either """
    """ always or under a particular condition """
    def __init__(self, size):
        self.name = None
        self.size = int(size)
        self.condition = None
        self.fields = []

    def add_field(self, name, msb, lsb):
        self.fields.append(Field(str(name), int(msb), int(lsb)))

    def is_valid(self):
        for f in self.fields:
            if f.msb < f.lsb: return False
            if f.lsb < 0: return False
            if f.msb > self.size: return False
        return True
