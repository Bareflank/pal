#ifndef PAL_EXECUTE_RDTSC_INLINE_H
#define PAL_EXECUTE_RDTSC_INLINE_H

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __cplusplus
static
#endif
inline uint64_t pal_execute_rdtsc_inline(void)
{
    uint64_t value = 0;

    __asm__ __volatile__(
        "rdtsc;"
        "shl {$32, %%rdx | rdx, 32};"
        "or {%%rdx, %%rax | rax, rdx};"
        "mov {%%rax, %[val] | %[val], rax};"
        : [val] "=r"(value)
        :
        : "rax", "rdx"
    );

    return value;
}

#ifdef __cplusplus
}
#endif

#endif
