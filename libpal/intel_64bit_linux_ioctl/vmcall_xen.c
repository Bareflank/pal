#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>

#include "devpal_abi_x64_intel.h"

#define DEVICE_FILE_NAME "/dev/devpal"

uint64_t pal_execute_vmcall_xen(uint64_t rax, uint64_t rdi, uint64_t rsi, uint64_t rdx, uint64_t r10, uint64_t r8, uint64_t r9)
{
    int file_desc;
    int status;
    struct vmcall_xen_operands vmcall_xen_ops = {0};

    file_desc = open(DEVICE_FILE_NAME, 0);
    if (file_desc < 0) {
        printf("[libpal] Can't open device file: %s\n", DEVICE_FILE_NAME);
        return -1;
    }

    vmcall_xen_ops.in.rax = rax;
    vmcall_xen_ops.in.rdi = rdi;
    vmcall_xen_ops.in.rsi = rsi;
    vmcall_xen_ops.in.rdx = rdx;
    vmcall_xen_ops.in.r10 = r10;
    vmcall_xen_ops.in.r8 = r8;
    vmcall_xen_ops.in.r9 = r9;

    if(ioctl(file_desc, DEVPAL_EXECUTE_VMCALL_XEN, &vmcall_xen_ops)) {
        printf("[libpal] vmcall_xen ioctl failed\n");
        return -1;
    }

    return vmcall_xen_ops.out.rax;
}
