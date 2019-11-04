from dataclasses import dataclass

from pal.gadget.gadget_properties import GadgetProperties

@dataclass
class properties(GadgetProperties):
    """ Properties of the include_guard gadget """

    gadget_name: str = "pal.include_guard"
    """ Name of the gadget these properties apply to """

    name: str = "PAL_H"
    """ The name of the include guard """

def include_guard(decorated):
    """
    A decorator gadget that generates include guards for C/C++ header files

    Usage:
        @include_guard
        function(generator, outfile, ...):
            outfile.write("contents protected by the include guard")

    Generates:
        #ifndef PAL_H
        #define PAL_H
        contents protected by the include guard
        #endif
    """
    def include_guard_decorator(generator, outfile, *args, **kwargs):
        properties = generator.gadgets["pal.include_guard"]
        writer = generator.get_writer()

        outfile.write("#ifndef " + str(properties.name) + "\n")
        outfile.write("#define " + str(properties.name) + "\n")
        writer.write_newline(outfile)

        decorated(generator, outfile, *args, **kwargs)
        outfile.write("#endif")
    return include_guard_decorator
