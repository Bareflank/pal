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

from shoulder.gadget.abstract_gadget import AbstractGadget
from shoulder.logger import logger
from shoulder.config import config
from shoulder.exception import *

class LicenseGadget(AbstractGadget):
    @property
    def description(self):
        return "Generate the Shoulder license for a C/C++ file"

    def generate(self, objects, outfile):
        try:
            with open(config.license_template_path, "r") as license:
                for line in license:
                    outfile.write("// " + line)
                outfile.write("\n")

            msg = "{gadget}: license generated".format(
                gadget = str(type(self).__name__)
            )
            logger.debug(msg)

        except Exception as e:
            msg = "{gadget} failed to generate license: {exception}".format(
                gadget = str(type(self).__name__),
                exception = e
            )
            raise ShoulderGeneratorException(msg)

def generate(objects, outfile):
    g = LicenseGadget()
    g.generate(objects, outfile)
