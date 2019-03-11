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

def include_guard(_decorated=None, *, name="SHOULDER_AARCH64_H"):
    """
    A decorator gadget that generates include guards for C/C++ header files

    Args:
        name (str): The name of the include guard to generate

    Usage:
        @include_guard(name=MY_INCLUDE_GUARD_H)
        function(generator, objects, outfile):
            outfile.write( <contents to be protected by the include guard> )
    """

    def _include_guard(decorated):
        def include_guard_decorator(generator, objects, outfile):
            outfile.write("#ifndef " + str(name) + "\n")
            outfile.write("#define " + str(name) + "\n\n")
            decorated(generator, objects, outfile)
            outfile.write("#endif\n")
        return include_guard_decorator

    if _decorated is None:
        return _include_guard
    else:
        return _include_guard(_decorated)
