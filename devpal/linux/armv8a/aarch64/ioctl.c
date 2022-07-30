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
long handle_devpal_ioctl_smc(struct smc_operands * user_ops);
long handle_devpal_ioctl_hvc(struct hvc_operands * user_ops);
long handle_devpal_ioctl_read_mem8(struct read_mem8_operands *user_ops);
long handle_devpal_ioctl_read_mem16(struct read_mem16_operands *user_ops);
long handle_devpal_ioctl_read_mem32(struct read_mem32_operands *user_ops);
long handle_devpal_ioctl_read_mem64(struct read_mem64_operands *user_ops);
long handle_devpal_ioctl_write_mem8(struct write_mem8_operands *user_ops);
long handle_devpal_ioctl_write_mem16(struct write_mem16_operands *user_ops);
long handle_devpal_ioctl_write_mem32(struct write_mem32_operands *user_ops);
long handle_devpal_ioctl_write_mem64(struct write_mem64_operands *user_ops);

long handle_devpal_ioctl(struct file *file, unsigned int cmd, unsigned long arg)
{
    printk("[devpal] ioctl: %u\n", cmd);

    switch (cmd) {
        case DEVPAL_EXECUTE_SYS:
            return handle_devpal_ioctl_sys((struct sys_operands *)arg);

        case DEVPAL_EXECUTE_SYSL:
            return handle_devpal_ioctl_sysl((struct sysl_operands *)arg);

        case DEVPAL_EXECUTE_SMC:
            return handle_devpal_ioctl_smc((struct smc_operands *)arg);

        case DEVPAL_EXECUTE_HVC:
            return handle_devpal_ioctl_hvc((struct hvc_operands *)arg);

        case DEVPAL_EXECUTE_READ_MEM8:
            return handle_devpal_ioctl_read_mem8((struct read_mem8_operands *)arg);

        case DEVPAL_EXECUTE_READ_MEM16:
            return handle_devpal_ioctl_read_mem16((struct read_mem16_operands *)arg);

        case DEVPAL_EXECUTE_READ_MEM32:
            return handle_devpal_ioctl_read_mem32((struct read_mem32_operands *)arg);

        case DEVPAL_EXECUTE_READ_MEM64:
            return handle_devpal_ioctl_read_mem64((struct read_mem64_operands *)arg);

        case DEVPAL_EXECUTE_WRITE_MEM8:
            return handle_devpal_ioctl_write_mem8((struct write_mem8_operands *)arg);

        case DEVPAL_EXECUTE_WRITE_MEM16:
            return handle_devpal_ioctl_write_mem16((struct write_mem16_operands *)arg);

        case DEVPAL_EXECUTE_WRITE_MEM32:
            return handle_devpal_ioctl_write_mem32((struct write_mem32_operands *)arg);

        case DEVPAL_EXECUTE_WRITE_MEM64:
            return handle_devpal_ioctl_write_mem64((struct write_mem64_operands *)arg);

        default:
            return -EINVAL;
    }
}
