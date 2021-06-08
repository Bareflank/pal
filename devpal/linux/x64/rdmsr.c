#include <linux/uaccess.h>
#include "devpal_abi_x64.h"

long handle_devpal_ioctl_rdmsr(struct rdmsr_operands * user_ops)
{
    uint64_t address = 0;
    uint64_t value = 0;
    struct rdmsr_operands kern_ops = {0};

    copy_from_user(&kern_ops, user_ops, sizeof(struct rdmsr_operands));
    address = kern_ops.in.address;

    __asm__ __volatile__(
        "mov %[addr], %%rcx;"
        "rdmsr;"
        "shl $32, %%rdx;"
        "or %%rdx, %%rax;"
        "mov %%rax, %[val];"
        : [val] "=r"(value)
        : [addr] "r"(address)
        : "rax", "rcx", "rdx"
    );

    kern_ops.out.value = value;
    copy_to_user(user_ops, &kern_ops, sizeof(struct rdmsr_operands));

    return 0;
}
