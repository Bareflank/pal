#include <linux/uaccess.h>
#include "devpal_abi_generic.h"

long handle_devpal_ioctl_write_mem8(struct write_mem8_operands * user_ops)
{
    struct write_mem8_operands kern_ops = {0};

    if (copy_from_user(&kern_ops, user_ops, sizeof(struct write_mem8_operands)))
        return -1;

    *((uint8_t *)kern_ops.in.address) = kern_ops.in.value ;

    return 0;
}
