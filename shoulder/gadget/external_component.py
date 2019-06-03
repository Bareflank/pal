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

import typing

from dataclasses import dataclass, field
from shoulder.gadget.gadget_properties import GadgetProperties

@dataclass
class properties(GadgetProperties):
    """ Properties of the external_component gadget """

    gadget_name: str = "shoulder.external_component"
    """ Name of the gadget these properties apply to """

    components: typing.List[str] = field(default_factory= lambda: [])
    """ List of unique components """

def external_component(decorated):
    """
    A decorator gadget that generates base address variables for each unique
    external component as well as a get() function

    Usage:
        @external_component
        function(generator, outfile, ...):
            outfile.write( <contents that depend on component base addresses> )
    """

    def external_component_decorator(generator, outfile, *args, **kwargs):
        properties = generator.gadgets["shoulder.external_component"]

        outfile.write("// External Component Base Addresses\n")

        for component in properties.components:
            outfile.write("static uintptr_t ")
            outfile.write(component + "_base = 0x0;\n")

        outfile.write("\n")

        decorated(generator, outfile, *args, **kwargs)

    return external_component_decorator



