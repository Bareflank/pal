import io

from pal.exception import *
from dataclasses import dataclass
from pal.gadget.gadget_properties import GadgetProperties

@dataclass
class properties(GadgetProperties):
    """ Properties of the Rust extern gadget """

    gadget_name: str = "pal.rust.extern"
    """ Name of the gadget these properties apply to """

    indent: int = 0
    """ The indentation level to generate at """

    indent_contents: bool = True
    """ Set True to indent extern contents one level above definition """

def extern(decorated):
    """
    A decorator gadget that generates a Rust extern {} block

    Usage:
        properties.name = "my::rust::extern"

        @extern
        function(generator, outfile, ...):
            outfile.write("contents inside generated extern block")

    Generates:
        extern {
            contents inside generated extern block
        }
    """
    def extern_decorator(generator, outfile, *args, **kwargs):
        properties = generator.gadgets["pal.rust.extern"]
        writer = generator.get_writer()

        writer.write_indent(outfile, count=properties.indent)

        outfile.write("extern {")
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

    return extern_decorator
