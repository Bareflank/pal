#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>

#include "devpal_abi_armv8a_aarch64.h"

#define DEVICE_FILE_NAME "/dev/devpal"

uint64_t pal_execute_sysl(uint8_t op1, uint8_t crn, uint8_t crm, uint8_t op2)
{
    int file_desc;
    int status;
    struct sysl_operands sysl_ops = {0};

    file_desc = open(DEVICE_FILE_NAME, 0);
    if (file_desc < 0) {
        printf("[libpal] Can't open device file: %s\n", DEVICE_FILE_NAME);
        return -1;
    }

    sysl_ops.in.op1 = op1;
    sysl_ops.in.crn = crn;
    sysl_ops.in.crm = crm;
    sysl_ops.in.op2 = op2;
    if(ioctl(file_desc, DEVPAL_EXECUTE_SYSL, &sysl_ops)) {
        printf("[libpal] sysl ioctl failed\n");
        return -1;
    }

    return sysl_ops.out.value;
}
