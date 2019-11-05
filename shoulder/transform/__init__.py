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

import collections

from .make_read_only import MakeReadOnly
from .make_write_only import MakeWriteOnly
from .quirks import Quirks
from .remove_coprocessor_am import RemoveCoprocessorAM
from .remove_implementation_defined import RemoveImplementationDefined
from .remove_memory_mapped_am import RemoveMemoryMappedAM
from .remove_redundant_am import RemoveRedundantAccessMechanisms
from .remove_redundant_fields import RemoveRedundantFields
from .remove_reserved_0 import RemoveReserved0
from .remove_reserved_1 import RemoveReserved1
from .remove_preserved import RemovePreserved
from .remove_reserved_sign_extended import RemoveReservedSignExtended
from .remove_system_banked_am import RemoveSystemBankedAM
from .remove_system_immediate_am import RemoveSystemImmediateAM
from .remove_system_register_am import RemoveSystemRegisterAM
from .remove_system_vector_am import RemoveSystemVectorAM
from .special_to_underscore import SpecialToUnderscore
from .unique_fieldset_names import UniqueFieldsetNames

# -----------------------------------------------------------------------------
# Module interface
# -----------------------------------------------------------------------------

# Usage:
#
# from shoulder.transform import transforms
# registers = transforms["name"].transform(registers)

transforms = collections.OrderedDict()

transforms["make_read_only"] = MakeReadOnly()
transforms["make_write_only"] = MakeWriteOnly()
transforms["quirks"] = Quirks()
transforms["remove_implementation_defined"] = RemoveImplementationDefined()
transforms["remove_coprocessor_am"] = RemoveCoprocessorAM()
transforms["remove_memory_mapped_am"] = RemoveMemoryMappedAM()
transforms["remove_system_register_am"] = RemoveSystemRegisterAM()
transforms["remove_system_banked_am"] = RemoveSystemBankedAM()
transforms["remove_system_immediate_am"] = RemoveSystemImmediateAM()
transforms["remove_system_vector_am"] = RemoveSystemVectorAM()
transforms["remove_redundant_am"] = RemoveRedundantAccessMechanisms()
transforms["remove_redundant_fields"] = RemoveRedundantFields()
transforms["remove_reserved_0"] = RemoveReserved0()
transforms["remove_reserved_1"] = RemoveReserved1()
transforms["remove_preserved"] = RemovePreserved()
transforms["remove_reserved_sign_extended"] = RemoveReservedSignExtended()
transforms["special_to_underscore"] = SpecialToUnderscore()
transforms["unique_fieldset_names"] = UniqueFieldsetNames()


def transform_all(registers):
    """ Apply all of the transforms to the given registers """
    for key, t in transforms.items():
        registers = t.transform(registers)
    return registers
