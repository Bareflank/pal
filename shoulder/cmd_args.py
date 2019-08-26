#
# Shoulder
# Copyright (C) 2018 Assured Information Security, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import getopt

from typing import List
from shoulder.config import config
from shoulder.logger import logger

# Available '-' arguments
short_opts = "i:o:"

# Available '--name=value' arguments
long_opts = []
for key, val in config.items():
    long_opts.append(str(key) + "=")

def print_usage():
    usage = "Usage:\n\tshoulder -i <path_to_register_spec> -o <outpath> [--config=value]"
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
                config.shoulder_output_dir = str(arg)
            else:
                opt_name = opt[2:]
                if config[opt_name]:
                    config[opt_name] = arg

    except getopt.GetoptError:
        logger.error("Invalid options specified, usage:")
        print_usage()
        print_options()
        sys.exit(2)

    return config
