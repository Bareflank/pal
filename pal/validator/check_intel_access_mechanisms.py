from pal.logger import logger

def check_intel_access_mechanisms_group(contents):
    logger.info("Validating source mnemonic")
    for file_index in range(len(contents)):
        check_access_mechanisms_functions(contents[file_index])
        check_access_mechanisms_names(contents[file_index])

# Used to read in control register for intel architecture
def check_access_mechanisms_functions(contents):
    # go through each file and check if the source_mnemonic matches
    name = contents.name
    # xcr0 in intel does not contain source_mnemonic or destination_mnemonic
    if name != "xcr0":
        read_source_mnemonic = contents.access_mechanisms["mov_read"][0].source_mnemonic
        write_destination_mnemonic = contents.access_mechanisms["mov_write"][0].destination_mnemonic

        if name != read_source_mnemonic:
            logger.error("Name does not match source_mnemonic")

        if name != write_destination_mnemonic:
            logger.error("Name does not match destination_mnemonic")

        if read_source_mnemonic != write_destination_mnemonic:
            logger.error("Read source mnemonic does not match write source mnemonic")


# make sure access mechanisms name matches mov_read/move_write, or, xsetbv/xgetbv
def check_access_mechanisms_names(contents):
    name = contents.name
    logger.info("Validating access mechanisms names in file: intel/" + name + ".yml")

    if name == "xcr0":
        access_mechanisms_read_name = contents.access_mechanisms["xgetbv"][0].name
        access_mechanisms_write_name = contents.access_mechanisms["xsetbv"][0].name
        if access_mechanisms_read_name != "xgetbv":
            logger.error("Access mechanism name [0] does not match 'mov_read': " + name + ".yml")
        if access_mechanisms_write_name != "xsetbv":
            logger.error("Access mechanism name [1] does not match 'mov_write': " + name + ".yml")
    else:
        access_mechanisms_read_name = contents.access_mechanisms["mov_read"][0].name
        access_mechanisms_write_name = contents.access_mechanisms["mov_write"][0].name
        if access_mechanisms_read_name != "mov_read":
            logger.error("Access mechanism name [0] does not match 'mov_read': " + name + ".yml")
        if access_mechanisms_write_name != "mov_write":
            logger.error("Access mechanism name [1] does not match 'mov_write': " + name + ".yml")