#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>

#include "devpal_abi_x64.h"

#define DEVICE_FILE_NAME "/dev/devpal"

uint64_t pal_execute_xgetbv(uint32_t xcr)
{
    int file_desc;
    int status;
    struct xgetbv_operands xgetbv_ops = {0};

    file_desc = open(DEVICE_FILE_NAME, 0);
    if (file_desc < 0) {
        printf("[libpal] Can't open device file: %s\n", DEVICE_FILE_NAME);
        return -1;
    }

    xgetbv_ops.in.xcr = xcr;
    if(ioctl(file_desc, DEVPAL_EXECUTE_XGETBV, &xgetbv_ops)) {
        printf("[libpal] xgetbv ioctl failed\n");
        return -1;
    }

    return xgetbv_ops.out.value;
}
