import yaml
from pal.logger import logger
from os import listdir
from os.path import isfile, join

def check_intel_access_mechanisms_group(indir):
    # Get all file names within the indir (Control Reg for Intel)
    intel_control_reg_files = [f for f in listdir(indir) if isfile(join(indir, f))]

    for file in intel_control_reg_files:
        contents = read_contents(file, indir)
        check_source_mnemonic(contents, file)
        check_access_mechanisms_names(contents, file)

def read_contents(fileName, directory):
    with open(directory + "/" + fileName) as file:
        return yaml.load(file, Loader=yaml.FullLoader)

# Used to read in control register for intel architecture
def check_source_mnemonic(contents, file):
    # go through each file and check if the source_mnemonic matches
    logger.info("Validating source mnemonic in file: intel/" + file)
    name = contents[0]["name"]
    # xcr0 in intel does not contain source_mnemonic or destination_mnemonic
    if name != "xcr0":
        read_source_mnemonic = contents[0]["access_mechanisms"][0]["source_mnemonic"]
        write_destination_mnemonic = contents[0]["access_mechanisms"][1]["destination_mnemonic"]

        if name != read_source_mnemonic:
            logger.error("Name does not match source_mnemonic")

        if name != write_destination_mnemonic:
            logger.error("Name does not match destination_mnemonic")

        if read_source_mnemonic != write_destination_mnemonic:
            logger.error("Read source mnemonic does not match write source mnemonic")

# make sure access mechanisms name matches mov_read/move_write, or, xsetbv/xgetbv
def check_access_mechanisms_names(contents, file):
    logger.info("Validating access mechanisms names in file: intel/" + file)
    name = contents[0]["name"]
    
    if name != "xcr0":
        if contents[0]["access_mechanisms"][0]["name"] != "mov_read":
            logger.error(file + " Access mechanism name [0] does not match 'mov_read'")
        if contents[0]["access_mechanisms"][1]["name"] != "mov_write":
            logger.error(file + " Access mechanism name [1] does not match 'mov_write'")
    elif name == "xcr0":
        if contents[0]["access_mechanisms"][0]["name"] != "xgetbv":
            logger.error(file + " Access mechanism name [0] does not match 'mov_read'")
        if contents[0]["access_mechanisms"][1]["name"] != "xsetbv":
            logger.error(file + " Access mechanism name [1] does not match 'mov_write'")