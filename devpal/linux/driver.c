#include <linux/fs.h>
#include <linux/module.h>
#include <linux/uaccess.h>
#include <linux/miscdevice.h>
#include <linux/kallsyms.h>
#include <linux/notifier.h>
#include <linux/reboot.h>
#include <linux/suspend.h>

#define DEVPAL_DEVICE_NAME "devpal"

extern long handle_devpal_ioctl(struct file *file, unsigned int cmd, unsigned long arg);
static long dev_unlocked_ioctl(struct file *file, unsigned int cmd, unsigned long arg)
{ return handle_devpal_ioctl(file, cmd, arg); }

static int dev_open(struct inode *inode, struct file *file)
{ return 0; }

static int dev_release(struct inode *inode, struct file *file)
{ return 0; }

static struct file_operations fops = {
    .open = dev_open,
    .release = dev_release,
    .unlocked_ioctl = dev_unlocked_ioctl,
};

static struct miscdevice executor_dev = {
    .minor = MISC_DYNAMIC_MINOR,
    .name = DEVPAL_DEVICE_NAME,
    .fops = &fops,
    .mode = 0666
};

int dev_reboot(struct notifier_block *nb, unsigned long code, void *unused)
{
    // Do stuff here if needed later
    return NOTIFY_DONE;
}

static int resume(void)
{
    // Do stuff here if needed later
    return NOTIFY_DONE;
}

static int suspend(void)
{
    // Do stuff here if needed later
    return NOTIFY_DONE;
}

int dev_pm(struct notifier_block *nb, unsigned long code, void *unused)
{
    switch (code) {
        case PM_SUSPEND_PREPARE:
        case PM_HIBERNATION_PREPARE:
        case PM_RESTORE_PREPARE:
            return suspend();

        case PM_POST_SUSPEND:
        case PM_POST_HIBERNATION:
        case PM_POST_RESTORE:
            return resume();

        default:
            break;
    }

    return NOTIFY_DONE;
}

static struct notifier_block reboot_notifier_block = {
    .notifier_call = dev_reboot
};

static struct notifier_block pm_notifier_block = {
    .notifier_call = dev_pm
};

int dev_init(void)
{
    register_reboot_notifier(&reboot_notifier_block);
    register_pm_notifier(&pm_notifier_block);

    if (misc_register(&executor_dev) != 0) {
        printk("misc_register failed\n");
        goto INIT_FAILURE;
    }

    // TODO: Set up the driver here

    printk("[devpal] driver loaded\n");

    return 0;

INIT_FAILURE:

    return -EPERM;
}

void dev_exit(void)
{
    // TODO: Tear down the driver here
    printk("[devpal] driver unloaded\n");

    misc_deregister(&executor_dev);
    unregister_pm_notifier(&pm_notifier_block);
    unregister_reboot_notifier(&reboot_notifier_block);

    return;
}

module_init(dev_init);
module_exit(dev_exit);

MODULE_LICENSE("GPL");

