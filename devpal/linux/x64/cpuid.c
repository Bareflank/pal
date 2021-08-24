#include <linux/uaccess.h>
#include "devpal_abi_x64.h"
#include "pal/instruction/cpuid_inline.h"

long handle_devpal_ioctl_cpuid(struct cpuid_operands * user_ops)
{
    struct cpuid_operands kern_ops = {0};
    pal_cpuid_return_values values = {0};

    copy_from_user(&kern_ops, user_ops, sizeof(struct cpuid_operands));

    values = pal_execute_cpuid_inline(kern_ops.in.leaf, kern_ops.in.subleaf);
    kern_ops.out.eax = values.eax;
    kern_ops.out.ebx = values.ebx;
    kern_ops.out.ecx = values.ecx;
    kern_ops.out.edx = values.edx;

    copy_to_user(user_ops, &kern_ops, sizeof(struct cpuid_operands));

    return 0;
}
