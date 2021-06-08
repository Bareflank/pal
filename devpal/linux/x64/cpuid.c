#include <linux/uaccess.h>
#include "devpal_abi_x64.h"

long handle_devpal_ioctl_cpuid(struct cpuid_operands * user_ops)
{
    uint32_t eax_in = 0;
    uint32_t ecx_in = 0;
    uint32_t eax_out = 0;
    uint32_t ebx_out = 0;
    uint32_t ecx_out = 0;
    uint32_t edx_out = 0;
    struct cpuid_operands kern_ops = {0};

    copy_from_user(&kern_ops, user_ops, sizeof(struct cpuid_operands));
    eax_in = kern_ops.in.leaf;
    ecx_in = kern_ops.in.subleaf;

    __asm__ __volatile__(
        "mov %[leaf], %%eax;"
        "mov %[subleaf], %%ecx;"
        "cpuid;"
        "mov %%eax, %[aout];"
        "mov %%ebx, %[bout];"
        "mov %%ecx, %[cout];"
        "mov %%edx, %[dout];"
        : [aout] "=r"(eax_out), [bout] "=r"(ebx_out), [cout] "=r"(ecx_out), [dout] "=r"(edx_out)
        : [leaf] "r"(eax_in), [subleaf] "r"(ecx_in)
        : "eax", "ebx", "ecx", "edx"
    );

    kern_ops.out.eax = eax_out;
    kern_ops.out.ebx = ebx_out;
    kern_ops.out.ecx = ecx_out;
    kern_ops.out.edx = edx_out;
    copy_to_user(user_ops, &kern_ops, sizeof(struct cpuid_operands));

    return 0;
}
