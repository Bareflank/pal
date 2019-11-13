import io

from pal.exception import *
from dataclasses import dataclass
from pal.gadget.gadget_properties import GadgetProperties

@dataclass
class properties(GadgetProperties):
    """ Properties of the namespace gadget """

    gadget_name: str = "pal.cxx.namespace"
    """ Name of the gadget these properties apply to """

    name: str = "pal"
    """ The name of the C++ namespace to generate """

    indent: int = 0
    """ The indentation level to generate at """

    indent_contents: bool = True
    """ Set True to indent namespace contents one level above definition """

def namespace(decorated):
    """
    A decorator gadget that generates a C++ namespace

    Usage:
        properties.name = "my::cxx::namespace"

        @namespace
        function(generator, outfile, ...):
            outfile.write("contents inside generated namespace")

    Generates:
        namespace my::cxx:namespace
        {
            contents inside generated namespace
        }
    """
    def namespace_decorator(generator, outfile, *args, **kwargs):
        properties = generator.gadgets["pal.cxx.namespace"]
        writer = generator.get_writer()

        writer.write_indent(outfile, count=properties.indent)

        outfile.write("namespace " + str(properties.name))
        writer.write_newline(outfile)

        writer.write_indent(outfile, count=properties.indent)
        outfile.write("{")
        writer.write_newline(outfile)

        contents = io.StringIO()
        decorated(generator, contents, *args, **kwargs)

        lines = contents.getvalue().splitlines()

        if len(lines) == 1:
            outfile.write(" ")
            outfile.write(lines[0])
            outfile.write(" ")

        elif len(lines) > 1:
            for line in lines:
                writer.write_indent(outfile, count=properties.indent)
                if properties.indent_contents:
                    outfile.write("    ")
                outfile.write(line + "\n")

        writer.write_indent(outfile, count=properties.indent)
        outfile.write("}")
        writer.write_newline(outfile)

    return namespace_decorator
