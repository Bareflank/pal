#ifndef PAL_EXECUTE_OUT_32_INLINE_H
#define PAL_EXECUTE_OUT_32_INLINE_H

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __cplusplus
static
#endif
inline void pal_execute_out_32_inline(uint16_t address, uint32_t value)
{
    __asm__ __volatile__(
        "mov {%[addr], %%dx | dx, %[addr]};"
        "mov {%[val], %%eax | eax, %[val]};"
        "{outl %%eax, %%dx | out dx, eax};"
        : 
        : [addr] "r"(address), [val] "r"(value)
        : "dx", "eax"
    );
}

#ifdef __cplusplus
}
#endif

#endif
