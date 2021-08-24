#ifndef PAL_EXECUTE_VMCALL_KVM_INLINE_H
#define PAL_EXECUTE_VMCALL_KVM_INLINE_H

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __cplusplus
static
#endif
uint64_t pal_execute_vmcall_kvm_inline(uint64_t rax, uint64_t rbx, uint64_t rcx, uint64_t rdx, uint64_t rsi)
{
    uint64_t rax_out = 0;

    __asm__ __volatile__(
        "mov {%[rax], %%rax | rax, %[rax]};"
        "mov {%[rbx], %%rbx | rbx, %[rbx]};"
        "mov {%[rcx], %%rcx | rcx, %[rcx]};"
        "mov {%[rdx], %%rdx | rdx, %[rdx]};"
        "mov {%[rsi], %%rsi | rsi, %[rsi]};"
        "vmcall;"
        "mov {%%rax, %[rax_out] | %[rax_out], rax};"
        : [rax_out] "=r"(rax_out)
        : [rax] "g"(rax), [rbx] "g"(rbx), [rcx] "g"(rcx), [rdx] "g"(rdx),
          [rsi] "g"(rsi)
        : "rax", "rbx", "rcx", "rdx", "rsi"
    );

    return rax_out;
}

#ifdef __cplusplus
}
#endif

#endif
