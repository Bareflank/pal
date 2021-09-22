#include <linux/uaccess.h>
#include "devpal_abi_x64_intel.h"
#include "pal/instruction/vmcall_xen_inline.h"

long handle_devpal_ioctl_vmcall_xen(struct vmcall_xen_operands * user_ops)
{

    struct vmcall_xen_operands kern_ops = {0};
    if (copy_from_user(&kern_ops, user_ops, sizeof(struct vmcall_xen_operands)))
        return -1;


    kern_ops.out.rax = pal_execute_vmcall_xen_inline(
            kern_ops.in.rax,
            kern_ops.in.rdi,
            kern_ops.in.rsi,
            kern_ops.in.rdx,
            kern_ops.in.r10,
            kern_ops.in.r8,
            kern_ops.in.r9
        );

    if (copy_to_user(user_ops, &kern_ops, sizeof(struct vmcall_xen_operands)))
        return -1;


    return 0;
}
