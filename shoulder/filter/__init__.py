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
# from shoulder.filters import filters
# registers = filters["filter_name"].filter_exclusive(registers)
# registers = filters["filter_name"].filter_inclusive(registers)

filters = OrderedDict()
filters["aarch32"] = aarch32.AArch32RegisterFilter()
filters["aarch64"] = aarch64.AArch64RegisterFilter()
filters["activity_monitor"] = activity_monitor.ActivityMonitorRegisterFilter()
filters["deprecated"] = deprecated.DeprecatedRegisterFilter()
filters["external"] = external.ExternalRegisterFilter()
filters["gic"] = gic.GICRegisterFilter()
filters["loregion"] = loregion.LORegionRegisterFilter()
filters["misc"] = misc.MiscelaneousRegisterFilter()
filters["mpam"] = mpam.MPAMRegisterFilter()
filters["no_access_mechanism"] = no_access_mechanism.NoAccessMechanismFilter()
filters["scxtnum"] = scxtnum.SCXTNUMRegisterFilter()
filters["statistical_profiling"] = \
    statistical_profiling.StatisticalProfilingRegisterFilter()
filters["sve"] = sve.SVERegisterFilter()
filters["trace"] = trace.TraceRegisterFilter()
filters["invalid"] = invalid.InvalidRegisterFilter()

def filter_all(registers):
    """ Apply all of the filters (exclusively) to the given registers """
    for key, f in filters.items():
        registers = f.filter_exclusive(registers)
    return registers
