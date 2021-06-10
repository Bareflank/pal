#include <linux/uaccess.h>
#include "devpal_abi_x64_intel.h"

long handle_devpal_ioctl_vmcall(struct vmcall_operands * user_ops)
{
    __asm__ __volatile__(
        "push %%rax;"
        "push %%rbx;"
        "push %%rcx;"
        "push %%rdx;"
        "push %%rsi;"
        "push %%rdi;"
        "push %%r8;"
        "push %%r9;"
        "push %%r10;"
        "push %%r11;"
        "push %%r12;"
        "push %%r13;"
        "push %%r14;"
        "push %%r15;"
        "push %%rbp;"
        "push %%rsp;"
        "vmcall;"
        "pop %%rsp;"
        "pop %%rbp;"
        "pop %%r15;"
        "pop %%r14;"
        "pop %%r13;"
        "pop %%r12;"
        "pop %%r11;"
        "pop %%r10;"
        "pop %%r9;"
        "pop %%r8;"
        "pop %%rdi;"
        "pop %%rsi;"
        "pop %%rdx;"
        "pop %%rcx;"
        "pop %%rbx;"
        "pop %%rax;"
        :
        :
        :
    );

    return 0;
}
