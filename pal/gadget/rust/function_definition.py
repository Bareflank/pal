import io
import typing

from dataclasses import dataclass, field
from pal.gadget.gadget_properties import GadgetProperties

@dataclass
class properties(GadgetProperties):
    """ Properties of the Rust function_definition gadget """

    gadget_name: str = "pal.rust.function_definition"
    """ The name of the Rust function to generate """

    name: str = "function_definition"
    """ The name of the Rust function to generate """

    args: typing.List[typing.Tuple[str, str]] = \
        field(default_factory= lambda: [])
    """ List of argmuent type/name tuples for the generated function """

    return_type: str = None
    """ Return type for the generated function """

    pub: bool = True
    """ Set True to declare function as pub """

    indent: int = 0
    """ The indentation level to generate at """

def function_definition(decorated):
    """
    A decorator gadget that generates a Rust function declaration. The function
    decorated by this gadget should generate the function's body.

    Usage:
        properties.name = "my_function"
        properties.return_type = "u64"
        properties.args = [("u64", "arg1")]

        @function_definition
        function(generator, outfile, ...):
            outfile.write("contents inside function body")

    Generates:
        pub fn my_function(arg1: u64) -> u64 {
            contents inside function body
        }
    """
    def function_definition_decorator(generator, outfile, *args, **kwargs):
        properties = generator.gadgets["pal.rust.function_definition"]
        writer = generator.get_writer()

        writer.write_indent(outfile, count=properties.indent)

        if properties.pub == True:
            outfile.write("pub ")

        outfile.write("fn ")
        outfile.write(str(properties.name))


        if len(properties.args) == 0:
            outfile.write("()")
        else:
            outfile.write("(")
            for idx, arg_pair in enumerate(properties.args):
                if idx > 0:
                    outfile.write(", ")
                outfile.write(str(arg_pair[1]) + ": ")
                outfile.write(str(arg_pair[0]))
            outfile.write(")")

        if properties.return_type:
            outfile.write(" -> " + str(properties.return_type) + " ")
        outfile.write(" {")
        writer.write_newline(outfile)

        contents = io.StringIO()
        decorated(generator, contents, *args, **kwargs)

        lines = contents.getvalue().splitlines()

        for line in lines:
            writer.write_indent(outfile, count=properties.indent + 1)
            outfile.write(line)
            writer.write_newline(outfile)

        writer.write_indent(outfile, count=properties.indent)
        outfile.write("}")
        writer.write_newline(outfile, count=2)

    return function_definition_decorator
