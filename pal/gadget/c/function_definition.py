import io
import typing

from dataclasses import dataclass, field
from pal.gadget.gadget_properties import GadgetProperties

@dataclass
class properties(GadgetProperties):
    """ Properties of the C function_definition gadget """

    gadget_name: str = "pal.c.function_definition"
    """ The name of the C function to generate """

    name: str = "function_definition"
    """ The name of the C function to generate """

    args: typing.List[typing.Tuple[str, str]] = \
        field(default_factory= lambda: [])
    """ List of argmuent type/name tuples for the generated function """

    return_type: str = "uint64_t"
    """ Return type for the generated function """

    inline: bool = True
    """ Set True to declare function as inline """

    indent: int = 0
    """ The indentation level to generate at """

def function_definition(decorated):
    """
    A decorator gadget that generates a C function declaration. The function
    decorated by this gadget should generate the function's body.

    Usage:
        properties.name = "my_function"
        properties.return_type = "uint64_t"
        properties.args = [("uint64_t", "arg1")]

        @function_definition
        function(generator, outfile, ...):
            outfile.write("contents inside function body")

    Generates:
        inline uint64_t my_function(uint64_t arg1)
        { contents inside function body }
    """
    def function_definition_decorator(generator, outfile, *args, **kwargs):
        properties = generator.gadgets["pal.c.function_definition"]
        writer = generator.get_writer()

        writer.write_indent(outfile, count=properties.indent)

        if properties.inline == True:
            outfile.write("static inline ")

        outfile.write(str(properties.return_type) + " ")
        outfile.write(str(properties.name))


        if len(properties.args) == 0:
            outfile.write("(void)")
            writer.write_newline(outfile)
        else:
            outfile.write("(")
            for idx, arg_pair in enumerate(properties.args):
                if idx > 0:
                    outfile.write(", ")
                outfile.write(str(arg_pair[0]) + " ")
                outfile.write(str(arg_pair[1]))
            outfile.write(")")
            writer.write_newline(outfile)

        writer.write_indent(outfile, count=properties.indent)
        outfile.write("{")

        contents = io.StringIO()
        decorated(generator, contents, *args, **kwargs)

        lines = contents.getvalue().splitlines()
        if len(lines) == 1:
            outfile.write(" ")
            outfile.write(lines[0])
            outfile.write(" ")
        elif len(lines) > 1:
            writer.write_newline(outfile)
            for line in lines:
                writer.write_indent(outfile, count=properties.indent + 1)
                outfile.write(line)
                writer.write_newline(outfile)
            writer.write_indent(outfile, count=properties.indent)

        outfile.write("}")
        writer.write_newline(outfile, count=2)

    return function_definition_decorator
