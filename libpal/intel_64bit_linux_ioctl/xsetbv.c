#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>

#include "devpal_abi_x64.h"

#define DEVICE_FILE_NAME "/dev/devpal"

void pal_execute_xsetbv_checked(uint32_t xcr, uint64_t value, uint64_t * error_out)
{
    int file_desc;
    int status;
    struct xsetbv_operands xsetbv_ops = {0};

    file_desc = open(DEVICE_FILE_NAME, 0);
    if (file_desc < 0) {
        printf("[libpal] Can't open device file: %s\n", DEVICE_FILE_NAME);
        if(error_out) *error_out = -1;
        return;
    }

    xsetbv_ops.in.xcr = xcr;
    xsetbv_ops.in.value = value;
    if(ioctl(file_desc, DEVPAL_EXECUTE_WRMSR, &xsetbv_ops)) {
        printf("[libpal] xsetbv ioctl failed\n");
        if(error_out) *error_out = -1;
        return;
    }
}

void pal_execute_xsetbv(uint32_t xcr, uint64_t value)
{ pal_execute_xsetbv_checked(xcr, value, NULL); }
