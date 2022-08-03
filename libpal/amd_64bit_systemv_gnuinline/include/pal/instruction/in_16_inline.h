#ifndef PAL_EXECUTE_IN_16_INLINE_H
#define PAL_EXECUTE_IN_16_INLINE_H

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __cplusplus
static
#endif
inline uint16_t pal_execute_in_16_inline(uint16_t address)
{
    uint16_t value = 0;

    __asm__ __volatile__(
        "mov {%[addr], %%dx | dx, %[addr]};"
        "{inw %%dx, %[val] | in %[val], dx};"
        : [val] "=r"(value)
        : [addr] "r"(address)
        : "dx"
    );

    return value;
}

#ifdef __cplusplus
}
#endif

#endif
