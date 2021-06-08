#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>

#include "devpal_abi_x64_intel.h"
#include "pal/instruction/vmcall.h"

#define DEVICE_FILE_NAME "/dev/devpal"

struct pal_vmcall_return_values pal_execute_vmcall(uint64_t rax, uint64_t rbx, uint64_t rcx, uint64_t rdx)
{
    int file_desc;
    int status;
    struct vmcall_operands vmcall_ops = {0};
    struct pal_vmcall_return_values values = {0};

    file_desc = open(DEVICE_FILE_NAME, 0);
    if (file_desc < 0) {
        printf("[libpal] Can't open device file: %s\n", DEVICE_FILE_NAME);
        return values;
    }

    vmcall_ops.in.rax = rax;
    vmcall_ops.in.rbx = rbx;
    vmcall_ops.in.rcx = rcx;
    vmcall_ops.in.rdx = rdx;
    vmcall_ops.in.rdi = rdi;
    vmcall_ops.in.rsi = rsi;
    vmcall_ops.in.r8 = r8;
    vmcall_ops.in.r9 = r9;
    vmcall_ops.in.r10 = r10;
    vmcall_ops.in.r11 = r11;

    if(ioctl(file_desc, DEVPAL_EXECUTE_VMCALL, &vmcall_ops)) {
        printf("[libpal] vmcall ioctl failed\n");
        return values;
    }

    values.rax = vmcall_ops.out.rax;
    values.rbx = vmcall_ops.out.rbx;
    values.rcx = vmcall_ops.out.rcx;
    values.rdx = vmcall_ops.out.rdx;
    values.rdi = vmcall_ops.out.rdi;
    values.rsi = vmcall_ops.out.rsi;
    values.r8 = vmcall_ops.out.r8;
    values.r9 = vmcall_ops.out.r9;
    values.r10 = vmcall_ops.out.r10;
    values.r11 = vmcall_ops.out.r11;
    return values;
}
