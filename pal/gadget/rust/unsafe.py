import io

from pal.exception import *
from dataclasses import dataclass
from pal.gadget.gadget_properties import GadgetProperties

@dataclass
class properties(GadgetProperties):
    """ Properties of the Rust unsafe gadget """

    gadget_name: str = "pal.rust.unsafe"
    """ Name of the gadget these properties apply to """

    indent: int = 0
    """ The indentation level to generate at """

    indent_contents: bool = True
    """ Set True to indent unsafe contents one level above definition """

def unsafe(decorated):
    """
    A decorator gadget that generates a Rust unsafe {} block

    Usage:
        properties.name = "my::rust::unsafe"

        @unsafe
        function(generator, outfile, ...):
            outfile.write("contents inside generated unsafe block")

    Generates:
        unsafe {
            contents inside generated unsafe block
        }
    """
    def unsafe_decorator(generator, outfile, *args, **kwargs):
        properties = generator.gadgets["pal.rust.unsafe"]
        writer = generator.get_writer()

        writer.write_indent(outfile, count=properties.indent)

        outfile.write("unsafe {")

        contents = io.StringIO()
        decorated(generator, contents, *args, **kwargs)

        lines = contents.getvalue().splitlines()

        if len(lines) == 0:
            outfile.write(" ")
        elif len(lines) == 1:
            outfile.write(" " + str(lines[0]) + " ")
        else:
            writer.write_newline(outfile)
            for line in lines:
                writer.write_indent(outfile, count=properties.indent)
                if properties.indent_contents:
                    writer.write_indent(outfile, count=1)
                outfile.write(line)
                writer.write_newline(outfile)
            writer.write_indent(outfile, count=properties.indent)

        outfile.write("}")
        writer.write_newline(outfile)

    return unsafe_decorator
