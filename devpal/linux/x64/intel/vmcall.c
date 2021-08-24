#include <linux/uaccess.h>
#include "devpal_abi_x64_intel.h"
#include "pal/instruction/vmcall_inline.h"

long handle_devpal_ioctl_vmcall(void)
{
    pal_execute_vmcall_inline();
    return 0;
}
