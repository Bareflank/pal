#include <linux/uaccess.h>
#include "devpal_abi_x64.h"
#include "pal/instruction/in_16_inline.h"

long handle_devpal_ioctl_in_16(struct in_16_operands * user_ops)
{
    struct in_16_operands kern_ops = {0};
    copy_from_user(&kern_ops, user_ops, sizeof(struct in_16_operands));

    kern_ops.out.value = pal_execute_in_16_inline(kern_ops.in.address);
    copy_to_user(user_ops, &kern_ops, sizeof(struct in_16_operands));

    return 0;
}
