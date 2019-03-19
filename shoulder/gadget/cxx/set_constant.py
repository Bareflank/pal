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

def set_constant(_decorated=None, *, indent=0, name="set"):
    """
    A decorator gadget that generates a function declaration for writing a
    constant (non-parameterized) value. The function decorated by this gadget
    should generate the function's body.

    Args:
        indent (int): The indentation level to generate at
        name (str): The name of the function to generate

    Usage:
        @set_constant
        function(generator, outfile, ...):
            outfile.write("contents inside function body")

    Generates:
        inline void set(void) noexcept
        { contents inside function body }
    """
    def _set_constant(decorated):
        def set_constant_decorator(generator, outfile, *args, **kwargs):
            indent_str = ""
            for level in range(0, indent):
                indent_str += "\t"

            outfile.write(indent_str)
            outfile.write("inline void " + name + "(void) noexcept")
            outfile.write("\n" + indent_str + "{ ")
            decorated(generator, outfile, *args, **kwargs)
            outfile.write(" }\n\n")
        return set_constant_decorator

    if _decorated is None:
        return _set_constant
    else:
        return _set_constant(_decorated)
