#include <linux/uaccess.h>
#include "devpal_abi_x64.h"
#include "pal/instruction/wrmsr_inline.h"

long handle_devpal_ioctl_wrmsr(struct wrmsr_operands * user_ops)
{
    struct wrmsr_operands kern_ops = {0};
    copy_from_user(&kern_ops, user_ops, sizeof(struct in_32_operands));
    pal_execute_wrmsr_inline(kern_ops.in.address, kern_ops.in.value);

    return 0;
}
