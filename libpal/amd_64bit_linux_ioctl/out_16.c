#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>

#include "devpal_abi_x64.h"

#define DEVICE_FILE_NAME "/dev/devpal"

void pal_execute_out_16_checked(uint16_t address, uint16_t value, uint64_t * error_out)
{
    int file_desc;
    int status;
    struct out_16_operands out_16_ops = {0};

    file_desc = open(DEVICE_FILE_NAME, 0);
    if (file_desc < 0) {
        printf("[libpal] Can't open device file: %s\n", DEVICE_FILE_NAME);
        if(error_out) *error_out = -1;
        return;
    }

    out_16_ops.in.address = address;
    out_16_ops.in.value = value;
    if(ioctl(file_desc, DEVPAL_EXECUTE_OUT_16, &out_16_ops)) {
        printf("[libpal] out_16 ioctl failed\n");
        if(error_out) *error_out = -1;
        return;
    }
}

void pal_execute_out_16(uint16_t address, uint16_t value)
{ pal_execute_out_16_checked(address, value, NULL); }
