from pal.logger import logger
import re
name_regex = "(leaf_[0-9|A-z]*_)"
name_hex_1 = "(leaf_)"
name_hex_2 = "(_e[a|b|c|d]x)"

def check_intel_cpuid_access_mechanisms_group(contents):
    logger.info("Validating CPUID access mechanism")
    for file_index in range(len(contents)):
        check_intel_cpuid_access_mechanisms(contents[file_index])

def convert_name_to_hex(name):
    name = re.sub(name_hex_1,"",name)
    name = re.sub(name_hex_2,"",name)
    name = "0x" + name
    name = int(name, 16)
    return name

# check access mechanisms against
def check_intel_cpuid_access_mechanisms(contents):
    name = contents.name
    name_hex = convert_name_to_hex(name)
    name = re.sub(name_regex, "", name)

    output = contents.access_mechanisms["cpuid"][0].output
    leaf = contents.access_mechanisms["cpuid"][0].leaf

    if(name != output):
        logger.error("Name does not match output for: intel/" + name + ".yml")

    if(name_hex != leaf):
        logger.error("Name hex value does not match leaf value in: intel/" + name + ".yml")
