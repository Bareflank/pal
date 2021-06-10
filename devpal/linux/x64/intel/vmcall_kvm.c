#include <linux/uaccess.h>
#include "devpal_abi_x64_intel.h"

long handle_devpal_ioctl_vmcall_kvm(struct vmcall_kvm_operands * user_ops)
{
    uint64_t rax_in = 0;
    uint64_t rbx_in = 0;
    uint64_t rcx_in = 0;
    uint64_t rdx_in = 0;
    uint64_t rsi_in = 0;

    uint64_t rax_out = 0;

    struct vmcall_kvm_operands kern_ops = {0};

    copy_from_user(&kern_ops, user_ops, sizeof(struct vmcall_kvm_operands));
    rax_in = kern_ops.in.rax;
    rbx_in = kern_ops.in.rbx;
    rcx_in = kern_ops.in.rcx;
    rdx_in = kern_ops.in.rdx;
    rsi_in = kern_ops.in.rsi;

    __asm__ __volatile__(
        "mov %[rax], %%rax;"
        "mov %[rbx], %%rbx;"
        "mov %[rcx], %%rcx;"
        "mov %[rdx], %%rdx;"
        "mov %[rsi], %%rsi;"
        "vmcall;"
        "mov %%rax, %[aout];"
        : [aout] "=r"(rax_out)
        : [rax] "r"(rax_in), [rbx] "r"(rbx_in), [rcx] "r"(rcx_in), [rdx] "r"(rdx_in),
          [rsi] "r"(rsi_in)
        : "rax", "rbx", "rcx", "rdx", "rsi"
    );

    kern_ops.out.rax = rax_out;
    copy_to_user(user_ops, &kern_ops, sizeof(struct vmcall_kvm_operands));

    return 0;
}
