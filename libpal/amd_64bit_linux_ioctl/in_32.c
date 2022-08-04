#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>

#include "devpal_abi_x64.h"

#define DEVICE_FILE_NAME "/dev/devpal"

uint32_t pal_execute_in_32(uint16_t address)
{
    int file_desc;
    int status;
    struct in_32_operands in_32_ops = {0};

    file_desc = open(DEVICE_FILE_NAME, 0);
    if (file_desc < 0) {
        printf("[libpal] Can't open device file: %s\n", DEVICE_FILE_NAME);
        return -1;
    }

    in_32_ops.in.address = address;
    if(ioctl(file_desc, DEVPAL_EXECUTE_IN_32, &in_32_ops)) {
        printf("[libpal] in_32 ioctl failed\n");
        return -1;
    }

    return in_32_ops.out.value;
}
