from dataclasses import dataclass

from pal.config import config
from pal.gadget.gadget_properties import GadgetProperties

@dataclass
class properties(GadgetProperties):
    """ Properties of the license gadget """

    gadget_name: str = "pal.license"
    """ Name of the gadget these properties apply to """

    path: str = config.license_template_path
    """ Path to a file that contains a license to be copied """

def license(decorated):
    """
    A decorator gadget that generates a license for source code files

    Usage:
        @license
        function(generator, outfile, ...):
            outfile.write( <generate other code that the license applies to> )
    """

    def license_decorator(generator, outfile, *args, **kwargs):
        properties = generator.gadgets["pal.license"]
        writer = generator.get_writer()

        with open(properties.path, "r") as license_file:
            outfile.write("/*\n")
            for line in license_file:
                outfile.write(" * " + line)
            outfile.write("*/\n")
        decorated(generator, outfile, *args, **kwargs)
    return license_decorator
