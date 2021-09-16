#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>

#include "devpal_abi_x64_intel.h"

#define DEVICE_FILE_NAME "/dev/devpal"

void pal_execute_vmwrite_checked(uint64_t encoding, uint64_t value, uint64_t * error_out)
{
    int file_desc;
    int status;
    struct vmwrite_operands vmwrite_ops = {0};

    file_desc = open(DEVICE_FILE_NAME, 0);
    if (file_desc < 0) {
        printf("[libpal] Can't open device file: %s\n", DEVICE_FILE_NAME);
        if(error_out) *error_out = -1;
        return;
    }

    vmwrite_ops.in.encoding = encoding;
    vmwrite_ops.in.value = value;
    if(ioctl(file_desc, DEVPAL_EXECUTE_VMWRITE, &vmwrite_ops)) {
        printf("[libpal] vmwrite ioctl failed\n");
        if(error_out) *error_out = -1;
        return;
    }
}

void pal_execute_vmwrite(uint32_t encoding, uint64_t value)
{ pal_execute_vmwrite_checked(encoding, value, NULL); }
