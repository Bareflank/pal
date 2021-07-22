#include <linux/uaccess.h>
#include "devpal_abi_generic.h"

long handle_devpal_ioctl_read_mem64(struct read_mem64_operands * user_ops)
{
    struct read_mem64_operands kern_ops = {0};

    copy_from_user(&kern_ops, user_ops, sizeof(struct read_mem64_operands));
    kern_ops.out.value = *((uint64_t *)kern_ops.in.address);
    copy_to_user(user_ops, &kern_ops, sizeof(struct read_mem64_operands));

    return 0;
}
