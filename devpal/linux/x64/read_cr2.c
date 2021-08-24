#include <linux/uaccess.h>
#include "devpal_abi_x64.h"
#include "pal/instruction/read_cr2_inline.h"

long handle_devpal_ioctl_read_cr2(struct read_cr2_operands * user_ops)
{
    struct read_cr2_operands kern_ops = {0};
    kern_ops.out.value = pal_execute_read_cr2_inline();
    copy_to_user(user_ops, &kern_ops, sizeof(struct read_cr2_operands));

    return 0;
}
