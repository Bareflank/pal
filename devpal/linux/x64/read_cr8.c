#include <linux/uaccess.h>
#include "devpal_abi_x64.h"

long handle_devpal_ioctl_read_cr8(struct read_cr8_operands * user_ops)
{
    uint64_t value = 0;
    struct read_cr8_operands kern_ops = {0};

    __asm__ __volatile__(
        "mov %%cr8, %[val];"
        : [val] "=r"(value)
        :
        :
    );

    kern_ops.out.value = value;
    copy_to_user(user_ops, &kern_ops, sizeof(struct read_cr8_operands));

    return 0;
}
