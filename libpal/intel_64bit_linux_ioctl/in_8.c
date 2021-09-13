#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>

#include "devpal_abi_x64.h"

#define DEVICE_FILE_NAME "/dev/devpal"

uint8_t pal_execute_in_8(uint16_t address)
{
    int file_desc;
    int status;
    struct in_8_operands in_8_ops = {0};

    file_desc = open(DEVICE_FILE_NAME, 0);
    if (file_desc < 0) {
        printf("[libpal] Can't open device file: %s\n", DEVICE_FILE_NAME);
        return -1;
    }

    in_8_ops.in.address = address;
    if(ioctl(file_desc, DEVPAL_EXECUTE_IN_8, &in_8_ops)) {
        printf("[libpal] in_8 ioctl failed\n");
        return -1;
    }

    return in_8_ops.out.value;
}
