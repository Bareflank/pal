#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>

#include "devpal_abi_generic.h"

#define DEVICE_FILE_NAME "/dev/devpal"

uint8_t pal_execute_read_mem8(uint64_t address)
{
    int file_desc;
    int status;
    struct read_mem8_operands read_mem8_ops = {0};

    file_desc = open(DEVICE_FILE_NAME, 0);
    if (file_desc < 0) {
        printf("[libpal] Can't open device file: %s\n", DEVICE_FILE_NAME);
        return -1;
    }

    read_mem8_ops.in.address = address;
    if(ioctl(file_desc, DEVPAL_EXECUTE_READ_MEM8, &read_mem8_ops)) {
        printf("[libpal] read_mem8 ioctl failed\n");
        return -1;
    }

    return read_mem8_ops.out.value;
}
