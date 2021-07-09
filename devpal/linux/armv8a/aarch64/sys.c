#include <linux/uaccess.h>
#include "devpal_abi_armv8a_aarch64.h"

long handle_devpal_ioctl_sys(struct sys_operands * user_ops)
{
    uint8_t op1 = 0;
    uint8_t crn = 0;
    uint8_t crm = 0;
    uint8_t op2 = 0;
    struct sys_operands kern_ops = {0};

    copy_from_user(&kern_ops, user_ops, sizeof(struct sys_operands));
    op1 = kern_ops.in.op1;
    crn = kern_ops.in.crn;
    crm = kern_ops.in.crm;
    op2 = kern_ops.in.op2;

    // TODO: Implement Me!
    // Is it possible to do the following?
    //  - take the fields that make up the encoding for the A64 SYS instruction
    //  - calculate the instruction encoding, and write it to memory
    //  - execute the instruction, using the memory value that just got written
    //  - return the value that the instruction outputs
    // __asm__ __volatile__(
    //     "sys;"
    //     :
    //     : [op1] "r"(op1), [crn] "r"(crn), [crm] "r"(crm), [op2] "r"(op2)
    //     :
    // );

    return 0;
}