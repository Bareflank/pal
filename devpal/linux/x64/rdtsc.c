#include <linux/uaccess.h>
#include "devpal_abi_x64.h"

long handle_devpal_ioctl_rdtsc(struct rdtsc_operands * user_ops)
{
    uint64_t value = 0;
    struct rdtsc_operands kern_ops = {0};

    __asm__ __volatile__(
        "rdtsc;"
        "shl $32, %%rdx;"
        "or %%rdx, %%rax;"
        "mov %%rax, %[val];"
        : [val] "=r"(value)
        :
        : "rax", "rdx"
    );

    kern_ops.out.value = value;
    copy_to_user(user_ops, &kern_ops, sizeof(struct rdtsc_operands));

    return 0;
}
