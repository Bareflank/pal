#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>

#include "devpal_abi_armv8a_aarch64.h"

#define DEVICE_FILE_NAME "/dev/devpal"

struct smc_operands pal_execute_smc(struct smc_operands *user_ops)
{
    int file_desc;
    int status;
    struct smc_operands smc_ops = {0};

    file_desc = open(DEVICE_FILE_NAME, 0);
    if (file_desc < 0)
    {
        printf("[libpal] Can't open device file: %s\n", DEVICE_FILE_NAME);
        return smc_ops;
    }

    smc_ops.in.W0 = (*user_ops).in.W0;
    smc_ops.in.X1 = (*user_ops).in.X1;
    smc_ops.in.X2 = (*user_ops).in.X2;
    smc_ops.in.X3 = (*user_ops).in.X3;
    smc_ops.in.X4 = (*user_ops).in.X4;
    smc_ops.in.X5 = (*user_ops).in.X5;
    smc_ops.in.X6 = (*user_ops).in.X6;
    smc_ops.in.X7 = (*user_ops).in.X7;
    smc_ops.in.X8 = (*user_ops).in.X8;
    smc_ops.in.X9 = (*user_ops).in.X9;
    smc_ops.in.X10 = (*user_ops).in.X10;
    smc_ops.in.X11 = (*user_ops).in.X11;
    smc_ops.in.X12 = (*user_ops).in.X12;
    smc_ops.in.X13 = (*user_ops).in.X13;
    smc_ops.in.X14 = (*user_ops).in.X14;
    smc_ops.in.X15 = (*user_ops).in.X15;
    smc_ops.in.X16 = (*user_ops).in.X16;
    smc_ops.in.X17 = (*user_ops).in.X17;
    
    if (ioctl(file_desc, DEVPAL_EXECUTE_SMC, &smc_ops))
    {
        printf("[libpal] smc ioctl failed\n");
        return smc_ops;
    }

    return smc_ops;
}