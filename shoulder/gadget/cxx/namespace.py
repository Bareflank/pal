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

from shoulder.exception import *

def namespace(_decorated=None, *, name=None, indent=0):
    """
    A decorator gadget that generates a C++ namespace

    Args:
        name (str): The name of the C++ namespace to generate (required)
        indent (int): The indentation level to generate at

    Usage:
        @namespace(name="my::cxx::namespace")
        function(generator, outfile, ...):
            outfile.write("contents inside generated namespace")

    Generates:
        my::cxx::namespace
        {
        contents inside generated namespace
        }
    """
    if not name:
        msg = "Must provide name argument for namespace gadget"
        raise ShoulderGeneratorException(msg)

    def _namespace(decorated):
        def namespace_decorator(generator, outfile, *args, **kwargs):
            indent_str = ""
            for level in range(0, indent):
                indent_str += "\t"

            outfile.write(indent_str)
            outfile.write("namespace " + str(name) + "\n")
            outfile.write(indent_str + "{\n")
            decorated(generator, outfile, *args, **kwargs)
            outfile.write(indent_str + "}\n\n")
        return namespace_decorator

    if _decorated is None:
        return _namespace
    else:
        return _namespace(_decorated)
