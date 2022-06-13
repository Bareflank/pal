#include <linux/uaccess.h>
#include "devpal_abi_armv8a_aarch64.h"

long handle_devpal_ioctl_sysl(struct sysl_operands * user_ops)
{
    uint8_t op1 = 0;
    uint8_t crn = 0;
    uint8_t crm = 0;
    uint8_t op2 = 0;
    uint64_t value = 0;
    struct sysl_operands kern_ops = {0};

    if (copy_from_user(&kern_ops, user_ops, sizeof(struct sysl_operands)))
        return -1;

    op1 = kern_ops.in.op1;
    crn = kern_ops.in.crn;
    crm = kern_ops.in.crm;
    op2 = kern_ops.in.op2;

    // TODO: Implement Me!
    //  - take the fields that make up the encoding for the A64 SYS instruction
    //  - calculate the instruction encoding
    //  - map the encoding to a function implemented within the driver

    kern_ops.out.value = value;
    if (copy_to_user(user_ops, &kern_ops, sizeof(struct sysl_operands)))
        return -1;

    return 0;
}
