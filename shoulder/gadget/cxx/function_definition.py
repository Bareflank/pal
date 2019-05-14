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
import typing

from dataclasses import dataclass, field
from shoulder.gadget.gadget_properties import GadgetProperties

@dataclass
class properties(GadgetProperties):
    """ Properties of the C++ function_definition gadget """

    gadget_name: str = "shoulder.cxx.function_definition"
    """ The name of the C function to generate """

    name: str = "function_definition"
    """ The name of the C function to generate """

    args: typing.List[typing.Tuple[str, str]] = \
        field(default_factory= lambda: [])
    """ List of argmuent type/name tuples for the generated function """

    return_type: str = "uint64_t"
    """ Return type for the generated function """

    inline: bool = True
    """ Set True to declare function as inline """

    const: bool = False
    """ Set True to declare function as const """

    noexcept: bool = False
    """ Set True to declare function as noexcept """

    indent: int = 0
    """ The indentation level to generate at """

def function_definition(decorated):
    """
    A decorator gadget that generates a C++ function declaration. The function
    decorated by this gadget should generate the function's body.

    Usage:
        properties.name = "my_function"
        properties.return_type = "uint64_t"
        properties.args = [("uint64_t", "arg1")]

        @function_definition
        function(generator, outfile, ...):
            outfile.write("contents inside function body")

    Generates:
        inline uint64_t my_function(uint64_t arg1)
        { contents inside function body }
    """
    def function_definition_decorator(generator, outfile, *args, **kwargs):
        properties = generator.gadgets["shoulder.cxx.function_definition"]

        indent_str = ""
        for level in range(0, properties.indent):
            indent_str += "\t"
        outfile.write(indent_str)

        if properties.inline == True:
            outfile.write("inline ")

        outfile.write(str(properties.return_type) + " ")
        outfile.write(str(properties.name))


        if len(properties.args) == 0:
            outfile.write("(void)\n")
        else:
            outfile.write("(")
            for idx, arg_pair in enumerate(properties.args):
                if idx > 0:
                    outfile.write(", ")
                outfile.write(str(arg_pair[0]) + " ")
                outfile.write(str(arg_pair[1]))
            outfile.write(")\n")

        outfile.write(indent_str + "{")
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

        outfile.write("}\n\n")

    return function_definition_decorator
