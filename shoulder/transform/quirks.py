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

from shoulder.transform.abstract_transform import AbstractTransform
from shoulder.logger import logger

class QuirksTransform(AbstractTransform):
    @property
    def description(self):
        return "fixing miscellaneous quirks from the XML specification"

    def do_transform(self, reg):
        if(reg.name == "FPEXC32_EL2"):
            for fs in reg.fieldsets:
                fs.fields = set([field for field in fs.fields if fs.fields.count(field.name) == "UFF"])
                logger.debug("Removed overlapping field \"UFF\" from register FPEXC32_EL2")

        if(reg.name == "HCR_EL2"):
            for fs in reg.fieldsets:
                for f_idx, f in enumerate(fs.fields):
                    if f.name == "TPC":
                        del fs.fields[f_idx]
                        logger.debug("Removed duplicate field \"TPC\" from register HCR_EL2")

        if(reg.name == "EDECCR"):
            for fs in reg.fieldsets:
                for f_idx, f in enumerate(fs.fields):
                    if f.name == "NSE":
                        del fs.fields[f_idx]
                        logger.debug("Removed overlapping field \"NSE\" from register EDECCR")

                for f_idx, f in enumerate(fs.fields):
                    if f.name == "SE":
                        del fs.fields[f_idx]
                        logger.debug("Removed overlapping field \"SE\" from register EDECCR")

        return reg
