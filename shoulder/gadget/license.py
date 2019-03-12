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

def license(_decorated=None, *, path=config.license_template_path):
    """
    A decorator gadget that generates a license for source code files

    Args:
        path (str): Path to a license file to be generated

    Usage:
        @license
        function(generator, objects, outfile):
            outfile.write( <generate other code that the license applies to> )
    """

    def _license(decorated):
        def license_decorator(generator, objects, outfile):
            with open(path, "r") as license_file:
                for line in license_file:
                    outfile.write("// " + line)
                outfile.write("\n")
            decorated(generator, objects, outfile)
        return license_decorator

    if _decorated is None:
        return _license
    else:
        return _license(_decorated)
