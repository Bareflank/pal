#include <linux/uaccess.h>
#include "devpal_abi_x64.h"
#include "pal/instruction/rdtsc_inline.h"

long handle_devpal_ioctl_rdtsc(struct rdtsc_operands * user_ops)
{
    struct rdtsc_operands kern_ops = {0};

    kern_ops.out.value = pal_execute_rdtsc_inline();
    copy_to_user(user_ops, &kern_ops, sizeof(struct rdtsc_operands));

    return 0;
}
