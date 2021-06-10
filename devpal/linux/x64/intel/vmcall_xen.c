#include <linux/uaccess.h>
#include "devpal_abi_x64_intel.h"

long handle_devpal_ioctl_vmcall_xen(struct vmcall_xen_operands * user_ops)
{
    uint64_t rax_in = 0;
    uint64_t rdi_in = 0;
    uint64_t rsi_in = 0;
    uint64_t rdx_in = 0;
    uint64_t r10_in = 0;
    uint64_t r8_in = 0;
    uint64_t r9_in = 0;

    uint64_t rax_out = 0;

    struct vmcall_xen_operands kern_ops = {0};

    copy_from_user(&kern_ops, user_ops, sizeof(struct vmcall_xen_operands));
    rax_in = kern_ops.in.rax;
    rdi_in = kern_ops.in.rdi;
    rsi_in = kern_ops.in.rsi;
    rdx_in = kern_ops.in.rdx;
    r10_in = kern_ops.in.r10;
    r8_in = kern_ops.in.r8;
    r9_in = kern_ops.in.r9;

    __asm__ __volatile__(
        "mov %[rax], %%rax;"
        "mov %[rdi], %%rdi;"
        "mov %[rsi], %%rsi;"
        "mov %[rdx], %%rdx;"
        "mov %[r10], %%r10;"
        "mov %[r8], %%r8;"
        "mov %[r9], %%r9;"
        "vmcall;"
        "mov %%rax, %[aout];"
        : [aout] "=r"(rax_out)
        : [rax] "r"(rax_in), [rdi] "r"(rdi_in), [rsi] "r"(rsi_in), [rdx] "r"(rdx_in),
          [r10] "r"(r10_in), [r8] "r"(r8_in), [r9] "r"(r9_in)
        : "rax", "rbx", "rcx", "rdx", "rsi"
    );

    kern_ops.out.rax = rax_out;
    copy_to_user(user_ops, &kern_ops, sizeof(struct vmcall_xen_operands));

    return 0;
}
