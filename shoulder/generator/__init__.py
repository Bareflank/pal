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

import os
import pkgutil

from shoulder.logger import logger
from shoulder.config import config
import shutil

pkg_dir = os.path.dirname(__file__)
for (module_loader, name, ispkg) in pkgutil.iter_modules([pkg_dir]):
    pkgutil.importlib.import_module('.' + name, __package__)

# -----------------------------------------------------------------------------
# Module interface
# -----------------------------------------------------------------------------

# Usage:
#
# from shoulder.generator import *
# generate_all()

def generate_all(objects, outdir):
    logger.info("Generating outputs to: " + str(outdir))

    all_generators = [cls for cls in abstract_generator.AbstractGenerator.__subclasses__()]

    for generator_class in all_generators:
        sub_outdir = os.path.abspath(os.path.join(outdir, generator_class.__name__))
        if not os.path.exists(sub_outdir):
                os.makedirs(sub_outdir)

        if os.path.exists(config.accessor_macros_path):
            shutil.copy(config.accessor_macros_path, sub_outdir)

        if os.path.exists(config.encoded_macros_path):
            shutil.copy(config.encoded_macros_path, sub_outdir)

        g = generator_class()
        g.generate(objects, sub_outdir)

    logger.info("Generation complete")
