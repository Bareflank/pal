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

from shoulder.config import config

def header_depends(decorated):
    """
    A decorator gadget that generates dependency-includes for C/C++ header files

    Usage:
        @header_depends
        function(generator, outfile, ...):
            outfile.write( <contents that depend on included headers> )
    """

    def header_depends_decorator(generator, outfile, *args, **kwargs):
        outfile.write("#include <stdint.h>\n")
        if config.encoded_functions:
            outfile.write("#include \"encoded_accessor_macros.h\"\n")
        outfile.write("#include \"aarch64_gcc_accessor_macros.h\"\n")
        outfile.write("\n")
        decorated(generator, outfile, *args, **kwargs)
    return header_depends_decorator

