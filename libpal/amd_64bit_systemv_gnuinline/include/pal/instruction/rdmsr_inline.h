#ifndef PAL_EXECUTE_RDMSR_INLINE_H
#define PAL_EXECUTE_RDMSR_INLINE_H

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __cplusplus
static
#endif
inline uint64_t pal_execute_rdmsr_inline(uint32_t address)
{
    uint64_t value;
    __asm__ __volatile__(
        "mov {%q[a], %%rcx | rcx, %q[a]};"
        "rdmsr;"
        "shl {$32, %%rdx | rdx, 32};"
        "or {%%rdx, %%rax | rax, rdx};"
        "mov {%%rax, %q[v] | %q[v], rax};"
        : [v] "=r"(value)
        : [a] "r"(address)
        : "rax", "rcx", "rdx"
    );
    return value;
}

#ifdef __cplusplus
}
#endif

#endif
