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

import json

from shoulder.parser.abstract_parser import AbstractParser
from shoulder.register import Register
from shoulder.fieldset import Fieldset
from shoulder.logger import logger
from shoulder.config import config

class IommuJsonParser(AbstractParser):
    @property
    def aarch_version_major(self):
        return 0

    @property
    def aarch_version_minor(self):
        return 0

    def parse_instructions(self, path):
        raise NotImplementedError(type(self).__name__ + ".parse_instructions not yet implemented")

    def parse_registers(self, path):
        registers = []

        with open(path, "r") as infile:
            content = json.load(infile)
            for reg in content:
                r = Register()
                r.name = reg["short_name"]
                r.long_name = reg["name"]
                r.size = reg["size"]
                r.offset = reg["offset"]

                fs = Fieldset(r.size)
                for field in reg["fields"]:
                    name = field["short_name"]
                    long_name = field["name"]
                    msb = field["msb"]
                    lsb = field["lsb"]
                    access = field["access"]
                    fs.add_field(name, msb, lsb, long_name=long_name, access=access)

                r.add_fieldset(fs)
                registers.append(r)

        return registers
