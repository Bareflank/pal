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

from shoulder.logger import logger
from shoulder.filters.abstract_filter import AbstractFilter

pkg_dir = os.path.dirname(__file__)
for (module_loader, name, ispkg) in pkgutil.iter_modules([pkg_dir]):
    pkgutil.importlib.import_module('.' + name, __package__)

all_filters = [cls for cls in abstract_filter.AbstractFilter.__subclasses__()]
all_filter_names = [f.__name__ for f in all_filters]

# -----------------------------------------------------------------------------
# Module interface
# -----------------------------------------------------------------------------

# Usage:
#
# from shoulder.filters import *
# apply_filters()

# Add any filters that need to be applied in a specific order by class name here
filters = []
filters.append("RemoveReservedFields")
filters.append("SpecialToUnderscore")
filters.append("Quirks")
filters.append("RemoveInvalidRegisters")
filters.append("RemoveDeprecatedRegisters")

# Any filters not listed above are run afterward in the order they were imported
filters = filters + list(set(all_filter_names) - set(filters))

# Delete any filters that need to be skipped by class name here
# ex: filters.remove("RemoveInvalidRegisters")

def apply_filters(objects):
    for f_name in filters:
        f_cls = next(x for x in all_filters if x.__name__ == f_name)
        f = f_cls()
        logger.info("Applying filter: {d}".format(d = str(f)))
        objects = f.do_filter(objects)

    return objects
