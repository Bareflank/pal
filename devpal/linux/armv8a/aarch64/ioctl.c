#include <linux/fs.h>
#include <linux/module.h>
#include <linux/uaccess.h>
#include <linux/miscdevice.h>
#include <linux/kallsyms.h>
#include <linux/notifier.h>
#include <linux/reboot.h>
#include <linux/suspend.h>
#include "devpal_abi.h"

long handle_devpal_ioctl_sys(struct sys_operands * user_ops);
long handle_devpal_ioctl_sysl(struct sysl_operands * user_ops);

long handle_devpal_ioctl(struct file *file, unsigned int cmd, unsigned long arg)
{
    printk("[devpal] ioctl: %u\n", cmd);
    switch (cmd) {
        case DEVPAL_EXECUTE_SYS:
            return handle_devpal_ioctl_sys((struct sys_operands *)arg);

        case DEVPAL_EXECUTE_SYSL:
            return handle_devpal_ioctl_sysl((struct sysl_operands *)arg);

        default:
            return -EINVAL;
    }
}
