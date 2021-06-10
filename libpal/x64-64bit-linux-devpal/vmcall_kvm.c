#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>

#include "devpal_abi_x64_intel.h"

#define DEVICE_FILE_NAME "/dev/devpal"

uint64_t pal_execute_vmcall_kvm(uint64_t rax, uint64_t rbx, uint64_t rcx, uint64_t rdx, uint64_t rsi)
{
    int file_desc;
    int status;
    struct vmcall_kvm_operands vmcall_kvm_ops = {0};

    file_desc = open(DEVICE_FILE_NAME, 0);
    if (file_desc < 0) {
        printf("[libpal] Can't open device file: %s\n", DEVICE_FILE_NAME);
        return -1;
    }

    vmcall_kvm_ops.in.rax = rax;
    vmcall_kvm_ops.in.rbx = rbx;
    vmcall_kvm_ops.in.rcx = rcx;
    vmcall_kvm_ops.in.rdx = rdx;
    vmcall_kvm_ops.in.rsi = rsi;

    if(ioctl(file_desc, DEVPAL_EXECUTE_VMCALL_KVM, &vmcall_kvm_ops)) {
        printf("[libpal] vmcall_kvm ioctl failed\n");
        return -1;
    }

    return vmcall_kvm_ops.out.rax;
}
