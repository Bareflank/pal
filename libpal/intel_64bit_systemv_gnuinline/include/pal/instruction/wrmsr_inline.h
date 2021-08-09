#ifndef PAL_EXECUTE_WRMSR_INLINE_H
#define PAL_EXECUTE_WRMSR_INLINE_H

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __cplusplus
static
#endif
inline void pal_execute_wrmsr_inline(uint32_t address, uint64_t value)
{
    __asm__ __volatile__(
        "mov {%q[a], %%rcx | rcx, %q[a]};"
        "mov {%[v], %%rax | rax, %[v]};"
        "mov {%[v], %%rdx | rdx, %[v]};"
        "shr {$32, %%rdx | rdx, 32};"
        "wrmsr;"
        : 
        : [a] "r"(address), [v] "r"(value)
        : "rax", "rcx", "rdx"
    );
}

#ifdef __cplusplus
}
#endif

#endif
