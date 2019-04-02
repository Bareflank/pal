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

import os
import sys
import pkgutil
from collections import OrderedDict

pkg_dir = os.path.dirname(__file__)
for (module_loader, name, ispkg) in pkgutil.iter_modules([pkg_dir]):
    pkgutil.importlib.import_module('.' + name, __package__)

# -----------------------------------------------------------------------------
# Module interface
# -----------------------------------------------------------------------------

# Usage:
#
# from shoulder.transform import transforms
# registers = transforms["name"].transform(registers)

transforms = OrderedDict()

transforms["n_counter_to_zero"] = n_counter_to_zero.NCounterToZero()
transforms["quirks"] = quirks.QuirksTransform()
transforms["remove_implementation_defined"] = \
    remove_implementation_defined.RemoveImplementationDefinedTransform()
transforms["remove_reserved_0"] = remove_reserved_0.RemoveReserved0Transform()
transforms["remove_reserved_1"] = remove_reserved_1.RemoveReserved1Transform()
transforms["special_to_underscore"] = \
    special_to_underscore.SpecialToUnderscoreTransform()

def transform_all(registers):
    """ Apply all of the transforms to the given registers """
    for key, t in transforms.items():
        registers = t.transform(registers)
    return registers
