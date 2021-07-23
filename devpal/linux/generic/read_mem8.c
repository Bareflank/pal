#include <linux/uaccess.h>
#include "devpal_abi_generic.h"

long handle_devpal_ioctl_read_mem8(struct read_mem8_operands * user_ops)
{
    struct read_mem8_operands kern_ops = {0};

    copy_from_user(&kern_ops, user_ops, sizeof(struct read_mem8_operands));
    kern_ops.out.value = *((uint8_t *)kern_ops.in.address);
    copy_to_user(user_ops, &kern_ops, sizeof(struct read_mem8_operands));

    return 0;
}