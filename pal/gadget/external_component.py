import typing

from dataclasses import dataclass, field
from pal.gadget.gadget_properties import GadgetProperties

@dataclass
class properties(GadgetProperties):
    """ Properties of the external_component gadget """

    gadget_name: str = "pal.external_component"
    """ Name of the gadget these properties apply to """

    components: typing.List[str] = field(default_factory= lambda: [])
    """ List of unique components """

def external_component(decorated):
    """
    A decorator gadget that generates base address variables for each unique
    external component as well as a get() function

    Usage:
        @external_component
        function(generator, outfile, ...):
            outfile.write( <contents that depend on component base addresses> )
    """

    def external_component_decorator(generator, outfile, *args, **kwargs):
        properties = generator.gadgets["pal.external_component"]

        outfile.write("// External Component Base Addresses\n")

        for component in properties.components:
            outfile.write("static uintptr_t ")
            outfile.write(component + "_base = 0x0;\n")

        outfile.write("\n")

        decorated(generator, outfile, *args, **kwargs)

    return external_component_decorator



