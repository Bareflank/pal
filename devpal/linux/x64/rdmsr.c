#include <linux/uaccess.h>
#include "devpal_abi_x64.h"
#include "pal/instruction/rdmsr_inline.h"

long handle_devpal_ioctl_rdmsr(struct rdmsr_operands * user_ops)
{
    struct rdmsr_operands kern_ops = {0};
    if (copy_from_user(&kern_ops, user_ops, sizeof(struct rdmsr_operands)))
        return -1;


    kern_ops.out.value = pal_execute_rdmsr_inline(kern_ops.in.address);
    if (copy_to_user(user_ops, &kern_ops, sizeof(struct rdmsr_operands)))
        return -1;


    return 0;
}
