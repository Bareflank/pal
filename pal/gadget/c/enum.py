import io

from dataclasses import dataclass
from pal.gadget.gadget_properties import GadgetProperties

@dataclass
class properties(GadgetProperties):
    """ Properties of the enum gadget """

    gadget_name: str = "pal.c.enum"
    """ Name of the gadget these properties apply to """

    name: str = ""
    """ If not empty, used as a name (typedef) for the enum """

    indent: int = 0
    """ The indentation level to generate at """

def enum(decorated):
    """
    A decorator gadget that generates a C enum declaration. The function
    decorated by this gadget should generate the enum's contents.

    Usage:
        properties.name = "my_enum"

        @enum
        function(generator, outfile, ...):
            outfile.write("contents,\ninside,\nthe,\nenum")

    Generates:
        typedef enum {
            contents,
            inside,
            the,
            enum
        } my_enum;
    """
    def enum_decorator(generator, outfile, *args, **kwargs):
        properties = generator.gadgets["pal.c.enum"]
        writer = generator.get_writer()

        writer.write_indent(outfile, count=properties.indent)

        if properties.name:
            outfile.write("typedef ")

        outfile.write("enum {")

        contents = io.StringIO()
        decorated(generator, contents, *args, **kwargs)

        lines = contents.getvalue().splitlines()
        if len(lines) == 1:
            outfile.write(" ")
            outfile.write(lines[0])
            outfile.write(" ")
        elif len(lines) > 1:
            writer.write_newline(outfile)
            writer.write_indent(outfile, count=properties.indent + 1)
            outfile.write(line)
            writer.write_newline(outfile)

        outfile.write("}")
        if properties.name:
            outfile.write(str(properties.name))
        outfile.write(";")
        writer.write_newline(outfile, count=2)

    return enum_decorator
