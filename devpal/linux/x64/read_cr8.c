#include <linux/uaccess.h>
#include "devpal_abi_x64.h"
#include "pal/instruction/read_cr8_inline.h"

long handle_devpal_ioctl_read_cr8(struct read_cr8_operands * user_ops)
{
    struct read_cr8_operands kern_ops = {0};
    kern_ops.out.value = pal_execute_read_cr8_inline();
    if (copy_to_user(user_ops, &kern_ops, sizeof(struct read_cr8_operands)))
        return -1;


    return 0;
}
