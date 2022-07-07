#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>

#include "devpal_abi_armv8a_aarch64.h"

#define DEVICE_FILE_NAME "/dev/devpal"

void pal_execute_sys(uint8_t op0, uint8_t op1, uint8_t crn, uint8_t crm, uint8_t op2, uint64_t value)
{
    int file_desc;
    int status;
    struct sys_operands sys_ops = {0};

    file_desc = open(DEVICE_FILE_NAME, 0);
    if (file_desc < 0) {
        printf("[libpal] Can't open device file: %s\n", DEVICE_FILE_NAME);
        return;
    }

    sys_ops.in.op0 = op0;
    sys_ops.in.op1 = op1;
    sys_ops.in.crn = crn;
    sys_ops.in.crm = crm;
    sys_ops.in.op2 = op2;
    sys_ops.in.value = value;
    if(ioctl(file_desc, DEVPAL_EXECUTE_SYS, &sys_ops)) {
        printf("[libpal] sys ioctl failed\n");
        return;
    }
}
