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

import abc

class AbstractParser(abc.ABC):
    @property
    @abc.abstractmethod
    def aarch_version_major(self):
        """ Major version of the ARM architecture specification """
        """ supported by this parser """
        pass

    @property
    @abc.abstractmethod
    def aarch_version_minor(self):
        """ Minor version of the ARM architecture specification """
        """ supported by this parser """
        pass

    @abc.abstractmethod
    def parse_registers(self, path):
        """ Parse the given file to a register object(s) """
        return

    @abc.abstractmethod
    def parse_instructions(self, path):
        """ Parse the given file to an instruction object(s) """
        return
