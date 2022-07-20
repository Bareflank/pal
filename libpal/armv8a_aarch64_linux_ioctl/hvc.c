#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>

#include "devpal_abi_armv8a_aarch64.h"

#define DEVICE_FILE_NAME "/dev/devpal"

struct hvc_operands pal_execute_hvc(struct hvc_operands *user_ops)
{
    int file_desc;
    int status;
    struct hvc_operands hvc_ops = {0};

    file_desc = open(DEVICE_FILE_NAME, 0);
    if (file_desc < 0)
    {
        printf("[libpal] Can't open device file: %s\n", DEVICE_FILE_NAME);
        return hvc_ops;
    }

    hvc_ops.in.W0 = (*user_ops).in.W0;
    hvc_ops.in.X1 = (*user_ops).in.X1;
    hvc_ops.in.X2 = (*user_ops).in.X2;
    hvc_ops.in.X3 = (*user_ops).in.X3;
    hvc_ops.in.X4 = (*user_ops).in.X4;
    hvc_ops.in.X5 = (*user_ops).in.X5;
    hvc_ops.in.X6 = (*user_ops).in.X6;
    hvc_ops.in.X7 = (*user_ops).in.X7;
    hvc_ops.in.X8 = (*user_ops).in.X8;
    hvc_ops.in.X9 = (*user_ops).in.X9;
    hvc_ops.in.X10 = (*user_ops).in.X10;
    hvc_ops.in.X11 = (*user_ops).in.X11;
    hvc_ops.in.X12 = (*user_ops).in.X12;
    hvc_ops.in.X13 = (*user_ops).in.X13;
    hvc_ops.in.X14 = (*user_ops).in.X14;
    
    if (ioctl(file_desc, DEVPAL_EXECUTE_HVC, &hvc_ops))
    {
        printf("[libpal] hvc ioctl failed\n");
        return hvc_ops;
    }

    return hvc_ops;
}