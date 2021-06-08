#include <linux/uaccess.h>
#include "devpal_abi_x64_intel.h"

long handle_devpal_ioctl_vmcall(struct vmcall_operands * user_ops)
{
    uint64_t rax_in = 0;
    uint64_t rbx_in = 0;
    uint64_t rcx_in = 0;
    uint64_t rdx_in = 0;
    uint64_t rdi_in = 0;
    uint64_t rsi_in = 0;
    uint64_t r8_in = 0;
    uint64_t r9_in = 0;
    uint64_t r10_in = 0;
    uint64_t r11_in = 0;

    uint64_t rax_out = 0;
    uint64_t rbx_out = 0;
    uint64_t rcx_out = 0;
    uint64_t rdx_out = 0;
    uint64_t rdi_out = 0;
    uint64_t rsi_out = 0;
    uint64_t r8_out = 0;
    uint64_t r9_out = 0;
    uint64_t r10_out = 0;
    uint64_t r11_out = 0;

    struct vmcall_operands kern_ops = {0};

    copy_from_user(&kern_ops, user_ops, sizeof(struct vmcall_operands));
    rax_in = kern_ops.in.rax;
    rbx_in = kern_ops.in.rbx;
    rcx_in = kern_ops.in.rcx;
    rdx_in = kern_ops.in.rdx;
    rdi_in = kern_ops.in.rdi;
    rsi_in = kern_ops.in.rsi;
    r8_in = kern_ops.in.r8;
    r9_in = kern_ops.in.r9;
    r10_in = kern_ops.in.r10;
    r11_in = kern_ops.in.r11;

    __asm__ __volatile__(
        "mov %[rax], %%rax;"
        "mov %[rbx], %%rbx;"
        "mov %[rcx], %%rcx;"
        "mov %[rdx], %%rdx;"
        "mov %[rdi], %%rdi;"
        "mov %[rsi], %%rsi;"
        "mov %[r8], %%r8;"
        "mov %[r9], %%r9;"
        "mov %[r10], %%r10;"
        "mov %[r11], %%r11;"
        "vmcall;"
        "mov %%rax, %[aout];"
        "mov %%rbx, %[bout];"
        "mov %%rcx, %[cout];"
        "mov %%rdx, %[dout];"
        "mov %%rdi, %[eout];"
        "mov %%rsi, %[fout];"
        "mov %%r8, %[gout];"
        "mov %%r9, %[hout];"
        "mov %%r10, %[iout];"
        "mov %%r11, %[jout];"
        : [aout] "=r"(rax_out), [bout] "=r"(rbx_out), [cout] "=r"(rcx_out), [dout] "=r"(rdx_out),
          [eout] "=r"(rdi_out), [fout] "=r"(rsi_out), [gout] "=r"(r8_out), [hout] "=r"(r9_out),
          [iout] "=r"(r10_out), [jout] "=r"(r11_out)
        : [rax] "r"(rax_in), [rbx] "r"(rbx_in), [rcx] "r"(rcx_in), [rdx] "r"(rdx_in),
          [rdi] "r"(rdi_in), [rsi] "r"(rsi_in), [r8] "r"(r8_in), [r9] "r"(r9_in),
          [r10] "r"(r10_in), [r11] "r"(r11_in)
        : "rax", "rbx", "rcx", "rdx"
    );

    kern_ops.out.rax = rax_out;
    kern_ops.out.rbx = rbx_out;
    kern_ops.out.rcx = rcx_out;
    kern_ops.out.rdx = rdx_out;
    kern_ops.out.rdi = rdi_out;
    kern_ops.out.rsi = rsi_out;
    kern_ops.out.r8 = r8_out;
    kern_ops.out.r9 = r9_out;
    kern_ops.out.r10 = r10_out;
    kern_ops.out.r11 = r11_out;
    copy_to_user(user_ops, &kern_ops, sizeof(struct vmcall_operands));

    return 0;
}
