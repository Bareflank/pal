#include <linux/uaccess.h>
#include "devpal_abi.h"

long handle_devpal_ioctl_vmmcall(struct vmmcall_operands * user_ops)
{
    // TODO: IOCTL handlers for AMD-specific system instructions should be
    // added to this directory. For example, the VMMCALL instruction
    return -1;
}
