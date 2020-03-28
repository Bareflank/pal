import sys
import getopt

from typing import List
from pal.config import config
from pal.logger import logger

# Available '-' arguments
short_opts = "i:o:"

# Available '--name=value' arguments
long_opts = []
for key, val in config.items():
    long_opts.append(str(key) + "=")

truthy_opts = ["true", "on", "1", "y", "yes"]
falsey_opts = ["false", "off", "0", "n", "no"]

def print_usage():
    usage = "Usage:\n\tpal -i <path_to_register_spec> -o <outpath> [--config=value]"
    print(usage)

def print_options():
    print("Available --config options:")
    for key, val in config.items():
        if val.options:
            options = str(val.options)
        elif type(val.default_value) == str:
            options = "<string>"
        else:
            options = ""

        msg = "\t--{name}={options}\n\t\t{desc}".format(
            name=str(key),
            options=options,
            desc=str(val.description)
        )
        print(msg)

def parse_cmd_args(args: List[str]) -> config:
    try:
        opts, args = getopt.getopt(args, short_opts, long_opts)

        for opt, arg in opts:
            if opt == "-i":
                config.xml_register_dir = str(arg)
            elif opt == "-o":
                config.pal_output_dir = str(arg)
            else:
                opt_name = opt[2:]
                if arg.lower() in truthy_opts:
                    config[opt_name] = True
                elif arg.lower() in falsey_opts:
                    config[opt_name] = False
                else:
                    config[opt_name] = arg

    except getopt.GetoptError:
        logger.error("Invalid options specified, usage:")
        print_usage()
        print_options()
        sys.exit(2)

    return config
