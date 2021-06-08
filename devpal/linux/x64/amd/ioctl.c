#include "devpal_abi.h"

// x86 Generic
long handle_devpal_ioctl_cpuid(struct cpuid_operands * user_ops);
long handle_devpal_ioctl_in_32(struct in_32_operands * user_ops);
long handle_devpal_ioctl_out_32(struct out_32_operands * user_ops);
long handle_devpal_ioctl_rdmsr(struct rdmsr_operands * user_ops);
long handle_devpal_ioctl_rdtsc(struct rdtsc_operands * user_ops);
long handle_devpal_ioctl_read_cr0(struct read_cr0_operands * user_ops);
long handle_devpal_ioctl_read_cr2(struct read_cr2_operands * user_ops);
long handle_devpal_ioctl_read_cr3(struct read_cr3_operands * user_ops);
long handle_devpal_ioctl_read_cr4(struct read_cr4_operands * user_ops);
long handle_devpal_ioctl_read_cr8(struct read_cr8_operands * user_ops);
long handle_devpal_ioctl_wrmsr(struct wrmsr_operands * user_ops);

// AMD specific
long handle_devpal_ioctl_vmmcall(struct vmmcall_operands * user_ops);

long handle_devpal_ioctl(struct file *file, unsigned int cmd, unsigned long arg)
{
    printk("[devpal] ioctl: %u\n", cmd);
    switch (cmd) {
        case DEVPAL_IOCTL_CPUID:
            return handle_devpal_ioctl_cpuid((struct cpuid_operands *)arg);

        case DEVPAL_IOCTL_IN_32:
            return handle_devpal_ioctl_in_32((struct in_32_operands *)arg);

        case DEVPAL_IOCTL_OUT_32:
            return handle_devpal_ioctl_out_32((struct out_32_operands *)arg);

        case DEVPAL_IOCTL_RDMSR:
            return handle_devpal_ioctl_rdmsr((struct rdmsr_operands *)arg);

        case DEVPAL_IOCTL_RDTSC:
            return handle_devpal_ioctl_rdtsc((struct rdtsc_operands *)arg);

        case DEVPAL_IOCTL_READ_CR0:
            return handle_devpal_ioctl_read_cr0((struct read_cr0_operands *)arg);

        case DEVPAL_IOCTL_READ_CR2:
            return handle_devpal_ioctl_read_cr2((struct read_cr2_operands *)arg);

        case DEVPAL_IOCTL_READ_CR3:
            return handle_devpal_ioctl_read_cr3((struct read_cr3_operands *)arg);

        case DEVPAL_IOCTL_READ_CR4:
            return handle_devpal_ioctl_read_cr4((struct read_cr4_operands *)arg);

        case DEVPAL_IOCTL_READ_CR8:
            return handle_devpal_ioctl_read_cr8((struct read_cr8_operands *)arg);

        case DEVPAL_IOCTL_VMCALL:
            return handle_devpal_ioctl_vmmcall((struct vmmcall_operands *)arg);

        case DEVPAL_IOCTL_WRMSR:
            return handle_devpal_ioctl_wrmsr((struct wrmsr_operands *)arg);

        default:
            return -EINVAL;
    }
}

