#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>

#include "devpal_abi_generic.h"

#define DEVICE_FILE_NAME "/dev/devpal"

void pal_execute_write_mem8(uint64_t address, uint8_t value)
{
    int file_desc;
    int status;
    struct write_mem8_operands write_mem8_ops = {0};

    file_desc = open(DEVICE_FILE_NAME, 0);
    if (file_desc < 0) {
        printf("[libpal] Can't open device file: %s\n", DEVICE_FILE_NAME);
        return;
    }

    write_mem8_ops.in.address = address;
    write_mem8_ops.in.value = value;
    if(ioctl(file_desc, DEVPAL_EXECUTE_WRITE_MEM8, &write_mem8_ops)) {
        printf("[libpal] write_mem8 ioctl failed\n");
        return;
    }
}
