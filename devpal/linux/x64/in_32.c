#include <linux/uaccess.h>
#include "devpal_abi_x64.h"

long handle_devpal_ioctl_in_32(struct in_32_operands * user_ops)
{
    uint16_t address = 0;
    uint32_t value = 0;
    struct in_32_operands kern_ops = {0};

    copy_from_user(&kern_ops, user_ops, sizeof(struct in_32_operands));
    address = kern_ops.in.address;

    __asm__ __volatile__(
        "mov %[addr], %%dx;"
        "in %%dx, %[val];"
        : [val] "=r"(value)
        : [addr] "r"(address)
        : "dx"
    );

    kern_ops.out.value = value;
    copy_to_user(user_ops, &kern_ops, sizeof(struct in_32_operands));

    return 0;
}
