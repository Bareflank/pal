from pal.logger import logger

def check_intel_msr_name_long_name_group(contents):
    logger.info("Validating MSR name against long_name")
    for file_index in range(len(contents)):
        check_name_against_long_name(contents[file_index])

def check_name_against_long_name(contents):
    name = contents.name
    long_name = contents.long_name
    if name != long_name:
        logger.warn("Name does not match long_name in: intel/" + name + ".yml")
