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

from shoulder.config import config
from shoulder.gadget.gadget_properties import GadgetProperties

@dataclass
class properties(GadgetProperties):
    """ Properties of the license gadget """

    gadget_name: str = "shoulder.license"
    """ Name of the gadget these properties apply to """

    path: str = config.license_template_path
    """ Path to a file that contains a license to be copied """

def license(decorated):
    """
    A decorator gadget that generates a license for source code files

    Usage:
        @license
        function(generator, outfile, ...):
            outfile.write( <generate other code that the license applies to> )
    """

    def license_decorator(generator, outfile, *args, **kwargs):
        properties = generator.gadgets["shoulder.license"]
        writer = generator.get_writer()

        with open(properties.path, "r") as license_file:
            outfile.write("/*\n")
            for line in license_file:
                outfile.write(" * " + line)
            outfile.write("*/\n")
        decorated(generator, outfile, *args, **kwargs)
    return license_decorator
