#ifndef PAL_EXECUTE_VMCALL_HYPERV_INLINE_H
#define PAL_EXECUTE_VMCALL_HYPERV_INLINE_H

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __cplusplus
static
#endif
uint64_t pal_execute_vmcall_hyperv_inline(uint64_t rcx, uint64_t rdx)
{
    uint64_t r8_out = 0;

    __asm__ __volatile__(
        "mov {%[rcx], %%rcx | rcx, %[rcx]};"
        "mov {%[rdx], %%rdx | rdx, %[rdx]};"
        "vmcall;"
        "mov {%%r8, %[r8_out] | %[r8_out], r8};"
        : [r8_out] "=r"(r8_out)
        : [rcx] "g"(rcx), [rdx] "g"(rdx)
        : "rcx", "rdx", "r8", "memory"
    );

    return r8_out;
}

#ifdef __cplusplus
}
#endif

#endif
