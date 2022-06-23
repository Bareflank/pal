#include <linux/uaccess.h>
#include "devpal_abi_armv8a_aarch64.h"

long handle_devpal_ioctl_sys(struct sys_operands * user_ops)
{
    uint8_t op1 = 0;
    uint8_t crn = 0;
    uint8_t crm = 0;
    uint8_t op2 = 0;
    uint64_t value = 0;
    struct sys_operands kern_ops = {0};

    if (copy_from_user(&kern_ops, user_ops, sizeof(struct sys_operands)))
        return -1;

    op1 = kern_ops.in.op1;
    crn = kern_ops.in.crn;
    crm = kern_ops.in.crm;
    op2 = kern_ops.in.op2;
    value = kern_ops.in.value;

    printk("Here: val= %llx", value);

    // inline assembly for msr
    __asm__ volatile("msr s3_0_c1_c0_0 , %0"
                     :
                     : "r"(value));


    return 0;
}
