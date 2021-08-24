#include <linux/fs.h>
#include <linux/module.h>
#include <linux/uaccess.h>
#include <linux/miscdevice.h>
#include <linux/kallsyms.h>
#include <linux/notifier.h>
#include <linux/reboot.h>
#include <linux/suspend.h>
#include "devpal_abi.h"

// x86 Generic
long handle_devpal_ioctl_cpuid(struct cpuid_operands * user_ops);
long handle_devpal_ioctl_in_8(struct in_8_operands * user_ops);
long handle_devpal_ioctl_in_16(struct in_16_operands * user_ops);
long handle_devpal_ioctl_in_32(struct in_32_operands * user_ops);
long handle_devpal_ioctl_out_8(struct out_8_operands * user_ops);
long handle_devpal_ioctl_out_16(struct out_16_operands * user_ops);
long handle_devpal_ioctl_out_32(struct out_32_operands * user_ops);
long handle_devpal_ioctl_rdmsr(struct rdmsr_operands * user_ops);
long handle_devpal_ioctl_rdtsc(struct rdtsc_operands * user_ops);
long handle_devpal_ioctl_read_cr0(struct read_cr0_operands * user_ops);
long handle_devpal_ioctl_read_cr2(struct read_cr2_operands * user_ops);
long handle_devpal_ioctl_read_cr3(struct read_cr3_operands * user_ops);
long handle_devpal_ioctl_read_cr4(struct read_cr4_operands * user_ops);
long handle_devpal_ioctl_read_cr8(struct read_cr8_operands * user_ops);
long handle_devpal_ioctl_wrmsr(struct wrmsr_operands * user_ops);

// Intel Specific
long handle_devpal_ioctl_vmcall(void);
long handle_devpal_ioctl_vmcall_kvm(struct vmcall_kvm_operands * user_ops);
long handle_devpal_ioctl_vmcall_xen(struct vmcall_xen_operands * user_ops);

long handle_devpal_ioctl(struct file *file, unsigned int cmd, unsigned long arg)
{
    printk("[devpal] ioctl: %u\n", cmd);
    switch (cmd) {
        case DEVPAL_EXECUTE_CPUID:
            return handle_devpal_ioctl_cpuid((struct cpuid_operands *)arg);

        case DEVPAL_EXECUTE_IN_8:
            return handle_devpal_ioctl_in_8((struct in_8_operands *)arg);

        case DEVPAL_EXECUTE_IN_16:
            return handle_devpal_ioctl_in_16((struct in_16_operands *)arg);

        case DEVPAL_EXECUTE_IN_32:
            return handle_devpal_ioctl_in_32((struct in_32_operands *)arg);

        case DEVPAL_EXECUTE_OUT_8:
            return handle_devpal_ioctl_out_8((struct out_8_operands *)arg);

        case DEVPAL_EXECUTE_OUT_16:
            return handle_devpal_ioctl_out_16((struct out_16_operands *)arg);

        case DEVPAL_EXECUTE_OUT_32:
            return handle_devpal_ioctl_out_32((struct out_32_operands *)arg);

        case DEVPAL_EXECUTE_RDMSR:
            return handle_devpal_ioctl_rdmsr((struct rdmsr_operands *)arg);

        case DEVPAL_EXECUTE_RDTSC:
            return handle_devpal_ioctl_rdtsc((struct rdtsc_operands *)arg);

        case DEVPAL_EXECUTE_READ_CR0:
            return handle_devpal_ioctl_read_cr0((struct read_cr0_operands *)arg);

        case DEVPAL_EXECUTE_READ_CR2:
            return handle_devpal_ioctl_read_cr2((struct read_cr2_operands *)arg);

        case DEVPAL_EXECUTE_READ_CR3:
            return handle_devpal_ioctl_read_cr3((struct read_cr3_operands *)arg);

        case DEVPAL_EXECUTE_READ_CR4:
            return handle_devpal_ioctl_read_cr4((struct read_cr4_operands *)arg);

        case DEVPAL_EXECUTE_READ_CR8:
            return handle_devpal_ioctl_read_cr8((struct read_cr8_operands *)arg);

        case DEVPAL_EXECUTE_VMCALL:
            return handle_devpal_ioctl_vmcall();

        case DEVPAL_EXECUTE_VMCALL_KVM:
            return handle_devpal_ioctl_vmcall_kvm((struct vmcall_kvm_operands *)arg);

        case DEVPAL_EXECUTE_VMCALL_XEN:
            return handle_devpal_ioctl_vmcall_xen((struct vmcall_xen_operands *)arg);

        case DEVPAL_EXECUTE_WRMSR:
            return handle_devpal_ioctl_wrmsr((struct wrmsr_operands *)arg);

        default:
            return -EINVAL;
    }
}

