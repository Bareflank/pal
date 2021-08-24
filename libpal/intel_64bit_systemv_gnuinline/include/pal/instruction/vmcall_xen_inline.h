#ifndef PAL_EXECUTE_VMCALL_XEN_INLINE_H
#define PAL_EXECUTE_VMCALL_XEN_INLINE_H

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __cplusplus
static
#endif
uint64_t pal_execute_vmcall_xen_inline(uint64_t rax, uint64_t rdi, uint64_t rsi, uint64_t rdx, uint64_t r10, uint64_t r8, uint64_t r9)
{
    uint64_t rax_out = 0;

    __asm__ __volatile__(
        "mov {%[rax], %%rax | rax, %[rax]};"
        "mov {%[rdi], %%rdi | rdi, %[rdi]};"
        "mov {%[rsi], %%rsi | rsi, %[rsi]};"
        "mov {%[rdx], %%rdx | rdx, %[rdx]};"
        "mov {%[r10], %%r10 | r10, %[r10]};"
        "mov {%[r8], %%r8 | r8, %[r8]};"
        "mov {%[r9], %%r9 | r9, %[r9]};"
        "vmcall;"
        "mov {%%rax, %[rax_out] | %[rax_out], rax};"
        : [rax_out] "=r"(rax_out)
        : [rax] "g"(rax), [rdi] "g"(rdi), [rsi] "g"(rsi), [rdx] "g"(rdx),
          [r10] "g"(r10), [r8] "g"(r8), [r9] "g"(r9)
        : "rax", "rcx", "rdx", "rdi", "rsi", "r8", "r9", "r10", "r11"
    );

    return rax_out;
}

#ifdef __cplusplus
}
#endif

#endif
