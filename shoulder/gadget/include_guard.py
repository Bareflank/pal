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

from shoulder.gadget.gadget_properties import GadgetProperties

@dataclass
class properties(GadgetProperties):
    """ Properties of the include_guard gadget """

    gadget_name: str = "shoulder.include_guard"
    """ Name of the gadget these properties apply to """

    name: str = "SHOULDER_AARCH64_H"
    """ The name of the include guard """

def include_guard(decorated):
    """
    A decorator gadget that generates include guards for C/C++ header files

    Usage:
        @include_guard
        function(generator, outfile, ...):
            outfile.write("contents protected by the include guard")

    Generates:
        #ifndef SHOULDER_AARCH64_H
        #define SHOULDER_AARCH64_H
        contents protected by the include guard
        #endif
    """
    def include_guard_decorator(generator, outfile, *args, **kwargs):
        properties = generator.gadgets["shoulder.include_guard"]

        outfile.write("#ifndef " + str(properties.name) + "\n")
        outfile.write("#define " + str(properties.name) + "\n\n")
        decorated(generator, outfile, *args, **kwargs)
        outfile.write("#endif\n")
    return include_guard_decorator
