#ifndef PAL_EXECUTE_CPUID_INLINE_H
#define PAL_EXECUTE_CPUID_INLINE_H

#ifdef __cplusplus
extern "C" {
#endif

typedef struct pal_cpuid_return_values {
    uint32_t eax;
    uint32_t ebx;
    uint32_t ecx;
    uint32_t edx;
} pal_cpuid_return_values;

#ifndef __cplusplus
static
#endif
inline pal_cpuid_return_values pal_execute_cpuid_inline(uint32_t eax, uint32_t ecx)
{
    uint32_t eax_out;
    uint32_t ebx_out;
    uint32_t ecx_out;
    uint32_t edx_out;
    __asm__ __volatile__(
        "mov {%[eax], %%eax | eax, %[eax]};"
        "mov {%[ecx], %%ecx | ecx, %[ecx]};"
        "cpuid;"
        "mov {%%eax, %[a] | %[a], eax};"
        "mov {%%ebx, %[b] | %[b], ebx};"
        "mov {%%ecx, %[c] | %[c], ecx};"
        "mov {%%edx, %[d] | %[d], edx};"
        : [a] "=r"(eax_out), [b] "=r"(ebx_out), [c] "=r"(ecx_out), [d] "=r"(edx_out)
        : [eax] "r"(eax), [ecx] "r"(ecx)
        : "eax", "ebx", "ecx", "edx"
    );
    return (pal_cpuid_return_values){.eax=eax_out, .ebx=ebx_out, .ecx=ecx_out, .edx=edx_out};
}

#ifdef __cplusplus
}
#endif

#endif
