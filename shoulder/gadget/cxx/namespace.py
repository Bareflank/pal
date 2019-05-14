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

import io

from shoulder.exception import *
from dataclasses import dataclass
from shoulder.gadget.gadget_properties import GadgetProperties

@dataclass
class properties(GadgetProperties):
    """ Properties of the namespace gadget """

    gadget_name: str = "shoulder.cxx.namespace"
    """ Name of the gadget these properties apply to """

    name: str = "shoulder"
    """ The name of the C++ namespace to generate """

    indent: int = 0
    """ The indentation level to generate at """

    indent_contents: bool = True
    """ Set True to indent namespace contents one level above definition """

def namespace(decorated):
    """
    A decorator gadget that generates a C++ namespace

    Usage:
        properties.name = "my::cxx::namespace"

        @namespace
        function(generator, outfile, ...):
            outfile.write("contents inside generated namespace")

    Generates:
        namespace my::cxx:namespace
        {
            contents inside generated namespace
        }
    """
    def namespace_decorator(generator, outfile, *args, **kwargs):
        properties = generator.gadgets["shoulder.cxx.namespace"]

        indent_str = ""
        for level in range(0, properties.indent):
            indent_str += "\t"

        outfile.write(indent_str)
        outfile.write("namespace " + str(properties.name) + "\n")
        outfile.write(indent_str + "{\n")

        contents = io.StringIO()
        decorated(generator, contents, *args, **kwargs)

        lines = contents.getvalue().splitlines()

        if len(lines) == 1:
            outfile.write(" ")
            outfile.write(lines[0])
            outfile.write(" ")

        elif len(lines) > 1:
            for line in lines:
                outfile.write(indent_str)
                if properties.indent_contents:
                    outfile.write("\t")
                outfile.write(line + "\n")

        outfile.write(indent_str + "}\n")

    return namespace_decorator
