#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>

#include "devpal_abi_x64_intel.h"

#define DEVICE_FILE_NAME "/dev/devpal"

uint64_t pal_execute_vmcall_hyperv(uint64_t rcx, uint64_t rdx)
{
    int file_desc;
    int status;
    struct vmcall_hyperv_operands vmcall_hyperv_ops = {0};

    file_desc = open(DEVICE_FILE_NAME, 0);
    if (file_desc < 0) {
        printf("[libpal] Can't open device file: %s\n", DEVICE_FILE_NAME);
        return -1;
    }

    vmcall_hyperv_ops.in.rcx = rcx;
    vmcall_hyperv_ops.in.rdx = rdx;

    if(ioctl(file_desc, DEVPAL_EXECUTE_VMCALL_KVM, &vmcall_hyperv_ops)) {
        printf("[libpal] vmcall_hyperv ioctl failed\n");
        return -1;
    }

    return vmcall_hyperv_ops.out.r8;
}
