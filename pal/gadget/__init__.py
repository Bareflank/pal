from .external_component import external_component
from .gadget_properties import GadgetProperties
from .header_depends import header_depends
from .include_guard import include_guard
from .license import license
from .c import *
from .cxx import *

from typing import List

def create_gadget_properties() -> List[GadgetProperties]:
    properties_subclasses = [cls for cls in GadgetProperties.__subclasses__()]
    properties = {}
    for subclass in properties_subclasses:
        p = subclass()
        properties[p.gadget_name] = p
    return properties
