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

from dataclasses import dataclass
from shoulder.gadget.gadget_properties import GadgetProperties

@dataclass
class properties(GadgetProperties):
    """ Properties of the enum gadget """

    gadget_name: str = "shoulder.c.enum"
    """ Name of the gadget these properties apply to """

    name: str = ""
    """ If not empty, used as a name (typedef) for the enum """

    indent: int = 0
    """ The indentation level to generate at """

def enum(decorated):
    """
    A decorator gadget that generates a C enum declaration. The function
    decorated by this gadget should generate the enum's contents.

    Usage:
        properties.name = "my_enum"

        @enum
        function(generator, outfile, ...):
            outfile.write("contents,\ninside,\nthe,\nenum")

    Generates:
        typedef enum {
            contents,
            inside,
            the,
            enum
        } my_enum;
    """
    def enum_decorator(generator, outfile, *args, **kwargs):
        properties = generator.gadgets["shoulder.c.enum"]

        indent_str = ""
        for level in range(0, properties.indent):
            indent_str += "\t"
        outfile.write(indent_str)

        if properties.name:
            outfile.write("typedef ")

        outfile.write("enum {")

        contents = io.StringIO()
        decorated(generator, contents, *args, **kwargs)

        lines = contents.getvalue().splitlines()
        if len(lines) == 1:
            outfile.write(" ")
            outfile.write(lines[0])
            outfile.write(" ")
        elif len(lines) > 1:
            outfile.write("\n")
            for line in lines:
                outfile.write(indent_str + "\t" + line + "\n")
            outfile.write(indent_str)

        outfile.write("}")
        if properties.name:
            outfile.write(str(properties.name))
        outfile.write(";\n\n")

    return enum_decorator
