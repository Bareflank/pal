import io
import typing

from dataclasses import dataclass, field
from pal.gadget.gadget_properties import GadgetProperties

@dataclass
class properties(GadgetProperties):
    """ Properties of the header_depends gadget """

    gadget_name: str = "pal.header_depends"
    """ Name of the gadget these properties apply to """

    includes: typing.List[str] = field(default_factory= lambda: [])
    """ List of include file paths """

def header_depends(decorated):
    """
    A decorator gadget that generates dependency-includes for C/C++ header files

    Usage:
        @header_depends
        function(generator, outfile, ...):
            outfile.write( <contents that depend on included headers> )
    """

    def header_depends_decorator(generator, outfile, *args, **kwargs):
        properties = generator.gadgets["pal.header_depends"]
        writer = generator.get_writer()

        for inc in  properties.includes:
            outfile.write("#include ")
            if inc.startswith("<"):
                outfile.write(str(inc) + "\n")
            else:
                outfile.write("\"" + str(inc) + "\"\n")
        writer.write_newline(outfile)
        decorated(generator, outfile, *args, **kwargs)
    return header_depends_decorator
