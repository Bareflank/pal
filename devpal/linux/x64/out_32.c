#include <linux/uaccess.h>
#include "devpal_abi_x64.h"
#include "pal/instruction/out_32_inline.h"

long handle_devpal_ioctl_out_32(struct out_32_operands * user_ops)
{
    struct out_32_operands kern_ops = {0};
    copy_from_user(&kern_ops, user_ops, sizeof(struct in_32_operands));

    pal_execute_out_32_inline(kern_ops.in.address, kern_ops.in.value);

    return 0;
}
