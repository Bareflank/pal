#include <linux/uaccess.h>
#include "devpal_abi_generic.h"

long handle_devpal_ioctl_write_mem64(struct write_mem64_operands * user_ops)
{
    struct write_mem64_operands kern_ops = {0};

    if (copy_from_user(&kern_ops, user_ops, sizeof(struct write_mem64_operands)))
        return -1;

    *((uint64_t *)kern_ops.in.address) = kern_ops.in.value ;

    return 0;
}
