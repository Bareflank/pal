#include <linux/uaccess.h>
#include "devpal_abi_x64_intel.h"
#include "pal/instruction/vmcall_kvm_inline.h"

long handle_devpal_ioctl_vmcall_kvm(struct vmcall_kvm_operands * user_ops)
{
    struct vmcall_kvm_operands kern_ops = {0};
    if (copy_from_user(&kern_ops, user_ops, sizeof(struct vmcall_kvm_operands)))
        return -1;


    kern_ops.out.rax = pal_execute_vmcall_kvm_inline(
            kern_ops.in.rax,
            kern_ops.in.rbx,
            kern_ops.in.rcx,
            kern_ops.in.rdx,
            kern_ops.in.rsi
        );

    if (copy_to_user(user_ops, &kern_ops, sizeof(struct vmcall_kvm_operands)))
        return -1;


    return 0;
}
