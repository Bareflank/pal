#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>

#include "devpal_abi_x64_intel.h"

#define DEVICE_FILE_NAME "/dev/devpal"

void pal_execute_vmcall(void)
{
    int file_desc;
    int status;
    struct vmcall_operands vmcall_ops;

    file_desc = open(DEVICE_FILE_NAME, 0);
    if (file_desc < 0) {
        printf("[libpal] Can't open device file: %s\n", DEVICE_FILE_NAME);
        return;
    }

    if(ioctl(file_desc, DEVPAL_EXECUTE_VMCALL, &vmcall_ops)) {
        printf("[libpal] vmcall ioctl failed\n");
        return;
    }
}
