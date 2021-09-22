#include <linux/uaccess.h>
#include "devpal_abi_x64_intel.h"
#include "pal/instruction/vmcall_hyperv_inline.h"

long handle_devpal_ioctl_vmcall_hyperv(struct vmcall_hyperv_operands * user_ops)
{
    struct vmcall_hyperv_operands kern_ops = {0};
    if (copy_from_user(&kern_ops, user_ops, sizeof(struct vmcall_hyperv_operands)))
        return -1;


    kern_ops.out.r8 = pal_execute_vmcall_hyperv_inline(
            kern_ops.in.rcx,
            kern_ops.in.rdx
        );

    if (copy_to_user(user_ops, &kern_ops, sizeof(struct vmcall_hyperv_operands)))
        return -1;


    return 0;
}
