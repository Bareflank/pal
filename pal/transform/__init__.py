import collections

from .insert_valid_first_character import InsertValidFirstCharacter
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
# from pal.transform import transforms
# registers = transforms["name"].transform(registers)

transforms = collections.OrderedDict()

transforms["insert_valid_first_character"] = InsertValidFirstCharacter()
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
