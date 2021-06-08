#include <linux/uaccess.h>
#include "devpal_abi_x64.h"

long handle_devpal_ioctl_read_cr4(struct read_cr4_operands * user_ops)
{
    uint64_t value = 0;
    struct read_cr4_operands kern_ops = {0};

    __asm__ __volatile__(
        "mov %%cr4, %[val];"
        : [val] "=r"(value)
        :
        :
    );

    kern_ops.out.value = value;
    copy_to_user(user_ops, &kern_ops, sizeof(struct read_cr4_operands));

    return 0;
}
