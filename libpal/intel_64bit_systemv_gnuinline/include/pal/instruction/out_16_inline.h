#ifndef PAL_EXECUTE_OUT_16_INLINE_H
#define PAL_EXECUTE_OUT_16_INLINE_H

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __cplusplus
static
#endif
inline void pal_execute_out_16_inline(uint16_t address, uint16_t value)
{
    __asm__ __volatile__(
        "mov {%[addr], %%dx | dx, %[addr]};"
        "mov {%[val], %%ax | ax, %[val]};"
        "{outw %%ax, %%dx | out dx, ax};"
        : 
        : [addr] "r"(address), [val] "r"(value)
        : "dx", "ax"
    );
}

#ifdef __cplusplus
}
#endif

#endif
