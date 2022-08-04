#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>

#include "devpal_abi_x64.h"

#define DEVICE_FILE_NAME "/dev/devpal"

uint64_t pal_execute_read_cr8(uint32_t address)
{
    int file_desc;
    int status;
    struct read_cr8_operands read_cr8_ops = {0};

    file_desc = open(DEVICE_FILE_NAME, 0);
    if (file_desc < 0) {
        printf("[libpal] Can't open device file: %s\n", DEVICE_FILE_NAME);
        return -1;
    }

    if(ioctl(file_desc, DEVPAL_EXECUTE_READ_CR8, &read_cr8_ops)) {
        printf("[libpal] read_cr8 ioctl failed\n");
        return -1;
    }

    return read_cr8_ops.out.value;
}
