#include <linux/uaccess.h>
#include "devpal_abi_x64.h"
#include "pal/instruction/in_8_inline.h"

long handle_devpal_ioctl_in_8(struct in_8_operands * user_ops)
{
    struct in_8_operands kern_ops = {0};
    if (copy_from_user(&kern_ops, user_ops, sizeof(struct in_8_operands)))
        return -1;


    kern_ops.out.value = pal_execute_in_8_inline(kern_ops.in.address);
    if (copy_to_user(user_ops, &kern_ops, sizeof(struct in_8_operands)))
        return -1;


    return 0;
}
