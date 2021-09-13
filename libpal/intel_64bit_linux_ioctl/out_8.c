#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>

#include "devpal_abi_x64.h"

#define DEVICE_FILE_NAME "/dev/devpal"

void pal_execute_out_8_checked(uint16_t address, uint8_t value, uint64_t * error_out)
{
    int file_desc;
    int status;
    struct out_8_operands out_8_ops = {0};

    file_desc = open(DEVICE_FILE_NAME, 0);
    if (file_desc < 0) {
        printf("[libpal] Can't open device file: %s\n", DEVICE_FILE_NAME);
        if(error_out) *error_out = -1;
        return;
    }

    out_8_ops.in.address = address;
    out_8_ops.in.value = value;
    if(ioctl(file_desc, DEVPAL_EXECUTE_OUT_8, &out_8_ops)) {
        printf("[libpal] out_8 ioctl failed\n");
        if(error_out) *error_out = -1;
        return;
    }
}

void pal_execute_out_8(uint16_t address, uint8_t value)
{ pal_execute_out_8_checked(address, value, NULL); }
