import os
import glob

from pal.logger import logger
from pal.exception import PalParserException
from pal.parser.armv8_xml_parser import ArmV8XmlParser
from pal.parser.pal_model_parser import PalModelParser

# -----------------------------------------------------------------------------
# Module interface
# -----------------------------------------------------------------------------

# Usage:
#
# from pal.parser import parse_registers
# regs = parse_registers("<path/to/xml/spec/register.xml>")


def parse_registers(spec_path):
    if not os.path.exists(spec_path):
        msg = "Failed to parse registers, spec not found at: " + str(spec_path)
        logger.error(msg)
        raise PalParserException(msg)

    logger.info("Parsing registers from: " + str(spec_path))

    regs = []

    #  paths = glob.glob(spec_path + "/*.xml")
    #  parser = ArmV8XmlParser()

    paths = glob.glob(spec_path + "/*.yml")
    parser = PalModelParser()

    for path in paths:
        results = parser.parse_file(path)
        if results:
            for result in results:
                regs.append(result)

    logger.debug("Registers parsed: " + str(len(regs)))
    return regs
