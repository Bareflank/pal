#include <linux/uaccess.h>
#include "devpal_abi_x64.h"

long handle_devpal_ioctl_wrmsr(struct wrmsr_operands * user_ops)
{
    uint32_t address = 0;
    uint64_t value = 0;
    struct wrmsr_operands kern_ops = {0};

    copy_from_user(&kern_ops, user_ops, sizeof(struct in_32_operands));
    address = kern_ops.in.address;
    value = kern_ops.in.value;

    __asm__ __volatile__(
        "mov %[val], %%rax;"
        "mov %[val], %%rdx;"
        "shr $32, %%rdx;"
        "mov %[addr], %%ecx;"
        "wrmsr;"
        : 
        : [val] "r"(value), [addr] "r"(address)
        : "rax", "ecx", "rdx"
    );

    return 0;
}
