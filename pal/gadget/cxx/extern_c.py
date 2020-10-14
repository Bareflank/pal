import io

from pal.exception import *
from dataclasses import dataclass
from pal.gadget.gadget_properties import GadgetProperties

@dataclass
class properties(GadgetProperties):
    """ Properties of the extern_c gadget """

    gadget_name: str = "pal.cxx.extern_c"
    """ Name of the gadget these properties apply to """

    indent: int = 0
    """ The indentation level to generate at """

    indent_contents: bool = True
    """ Set True to indent extern C contents one level above definition """

def extern_c(decorated):
    """
    A decorator gadget that generates a C++ extern "C" {} block

    Usage:
        properties.name = "my::cxx::extern_c"

        @extern_c
        function(generator, outfile, ...):
            outfile.write("contents inside generated extern C block")

    Generates:
        extern "C" {
            contents inside generated extern C block
        }
    """
    def extern_c_decorator(generator, outfile, *args, **kwargs):
        properties = generator.gadgets["pal.cxx.extern_c"]
        writer = generator.get_writer()

        writer.write_indent(outfile, count=properties.indent)

        outfile.write("extern \"C\" {")
        writer.write_newline(outfile)

        contents = io.StringIO()
        decorated(generator, contents, *args, **kwargs)

        lines = contents.getvalue().splitlines()

        for line in lines:
            writer.write_indent(outfile, count=properties.indent)
            if properties.indent_contents:
                writer.write_indent(outfile, count=1)
            outfile.write(line)
            writer.write_newline(outfile)

        writer.write_indent(outfile, count=properties.indent)
        outfile.write("}")
        writer.write_newline(outfile)

    return extern_c_decorator
