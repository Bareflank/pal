#ifndef PAL_EXECUTE_OUT_8_INLINE_H
#define PAL_EXECUTE_OUT_8_INLINE_H

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __cplusplus
static
#endif
inline void pal_execute_out_8_inline(uint16_t address, uint8_t value)
{
    __asm__ __volatile__(
        "mov {%[addr], %%dx | dx, %[addr]};"
        "mov {%[val], %%al | al, %[val];"
        "{outl %%al, %%dx | out dx, al};"
        : 
        : [addr] "r"(address), [val] "r"(value)
        : "dx", "al"
    );
}

#ifdef __cplusplus
}
#endif

#endif
