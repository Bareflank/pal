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

def get_32_from_value(_decorated=None, *, indent=0, name="get", arg="val"):
    """
    A decorator gadget that generates a function declaration for reading a
    32-bit result from a given 32-bit value. The function decorated by this
    gadget should generate the function's body.

    Args:
        indent (int): The indentation level to generate at
        name (str): The name of the function to generate
        arg (str): The name of the function argument to generate

    Usage:
        @get_32_from_value
        function(generator, outfile, ...):
            outfile.write("contents inside function body")

    Generates:
        inline uint32_t get(uint32_t val) noexcept
        { contents inside function body }
    """
    def _get_32_from_value(decorated):
        def get_32_from_value_decorator(generator, outfile, *args, **kwargs):
            indent_str = ""
            for level in range(0, indent):
                indent_str += "\t"

            outfile.write(indent_str)
            outfile.write("inline uint32_t " + str(name))
            outfile.write("(uint32_t " + str(arg) +") noexcept")
            outfile.write("\n" + indent_str + "{ ")
            decorated(generator, outfile, *args, **kwargs)
            outfile.write(" }\n\n")
        return get_32_from_value_decorator

    if _decorated is None:
        return _get_32_from_value
    else:
        return _get_32_from_value(_decorated)
