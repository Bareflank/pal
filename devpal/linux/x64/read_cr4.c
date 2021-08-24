#include <linux/uaccess.h>
#include "devpal_abi_x64.h"
#include "pal/instruction/read_cr4_inline.h"

long handle_devpal_ioctl_read_cr4(struct read_cr4_operands * user_ops)
{
    struct read_cr4_operands kern_ops = {0};
    kern_ops.out.value = pal_execute_read_cr4_inline();
    copy_to_user(user_ops, &kern_ops, sizeof(struct read_cr4_operands));

    return 0;
}
