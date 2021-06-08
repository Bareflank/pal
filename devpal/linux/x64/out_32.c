#include <linux/uaccess.h>
#include "devpal_abi_x64.h"

long handle_devpal_ioctl_out_32(struct out_32_operands * user_ops)
{
    uint16_t address = 0;
    uint32_t value = 0;
    struct out_32_operands kern_ops = {0};

    copy_from_user(&kern_ops, user_ops, sizeof(struct in_32_operands));
    address = kern_ops.in.address;
    value = kern_ops.in.value;

    __asm__ __volatile__(
        "mov %[addr], %%dx;"
        "mov %[val], %%eax;"
        "out %%eax, %%dx;"
        : 
        : [addr] "r"(address), [val] "r"(value)
        : "dx", "eax"
    );

    return 0;
}
