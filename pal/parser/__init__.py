import os
import glob

from pal.logger import logger
from pal.exception import PalParserException
from pal.parser.armv8_xml_parser import ArmV8XmlParser
from pal.parser.pal_model_parser import PalModelParser
from pal.parser.pal_instruction_model_parser import PalInstructionModelParser

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


def parse_instructions(spec_path):
    if not os.path.exists(spec_path):
        msg = "Failed to parse instructions, spec not found at: " + str(spec_path)
        logger.error(msg)
        raise PalParserException(msg)

    logger.info("Parsing instructions from: " + str(spec_path))

    instructions = []

    paths = glob.glob(spec_path + "/*.yml")
    parser = PalInstructionModelParser()

    for path in paths:
        results = parser.parse_instructions_from_file(path)
        if results:
            for result in results:
                instructions.append(result)

    logger.debug("Instructions parsed: " + str(len(instructions)))
    return instructions
