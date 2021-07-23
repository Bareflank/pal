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
# from pal.filters import filters
# registers = filters["filter_name"].filter_exclusive(registers)
# registers = filters["filter_name"].filter_inclusive(registers)

filters = OrderedDict()
filters["aarch32"] = aarch32.AArch32RegisterFilter()
filters["aarch64"] = aarch64.AArch64RegisterFilter()
filters["activity_monitor"] = activity_monitor.ActivityMonitorRegisterFilter()
filters["deprecated"] = deprecated.DeprecatedRegisterFilter()
filters["external"] = external.ExternalRegisterFilter()
filters["gic"] = gic.GICRegisterFilter()
filters["irregular_size"] = irregular_size.IrregularSizeFilter()
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
