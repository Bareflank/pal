#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>

#include "devpal_abi_x64_intel.h"

#define DEVICE_FILE_NAME "/dev/devpal"

uint64_t pal_execute_vmread(uint64_t encoding)
{
    int file_desc;
    int status;
    struct vmread_operands vmread_ops = {0};

    file_desc = open(DEVICE_FILE_NAME, 0);
    if (file_desc < 0) {
        printf("[libpal] Can't open device file: %s\n", DEVICE_FILE_NAME);
        return -1;
    }

    vmread_ops.in.encoding = encoding;
    if(ioctl(file_desc, DEVPAL_EXECUTE_VMREAD, &vmread_ops)) {
        printf("[libpal] vmread ioctl failed\n");
        return -1;
    }

    return vmread_ops.out.value;
}
