#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>

#include "devpal_abi_generic.h"

#define DEVICE_FILE_NAME "/dev/devpal"

uint16_t pal_execute_read_mem16(uint64_t address)
{
    int file_desc;
    int status;
    struct read_mem16_operands read_mem16_ops = {0};

    file_desc = open(DEVICE_FILE_NAME, 0);
    if (file_desc < 0) {
        printf("[libpal] Can't open device file: %s\n", DEVICE_FILE_NAME);
        return -1;
    }

    read_mem16_ops.in.address = address;
    if(ioctl(file_desc, DEVPAL_EXECUTE_READ_MEM16, &read_mem16_ops)) {
        printf("[libpal] read_mem16 ioctl failed\n");
        return -1;
    }

    return read_mem16_ops.out.value;
}
