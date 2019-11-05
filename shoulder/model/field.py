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

from dataclasses import dataclass


@dataclass
class Field():
    """ Models a single named field (or bitfield) in a register fieldset """

    name: str = ""
    """ The abbreviated/symbolic/accronym name for this field """

    msb: int = 0
    """ Most significant bit that the field occupies within a register """

    lsb: int = 0
    """ Least significant bit that the field occupies within a register """

    long_name: str = ""
    """ The non-abbreviated/spelled out name for this field """

    description: str = ""
    """ A description of this field """

    readable: bool = False
    """ True if this field is readable  """

    writable: bool = False
    """ True if this field is writable  """

    lockable: bool = False
    """ True if this field can be locked  """

    write_once: bool = False
    """ True if this field becomes locked after writing to it once  """

    write_1_clear: bool = False
    """ True if this field is cleared (set to '0') by writing a '1' to it  """

    reserved0: bool = False
    """ True if the value of this field is reserved 0  """

    reserved1: bool = False
    """ True if the value of this field is reserved 1  """

    preserved: bool = False
    """ True if the value of this field should be preserved across writes  """
