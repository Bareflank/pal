#ifndef PAL_EXECUTE_IN_32_INLINE_H
#define PAL_EXECUTE_IN_32_INLINE_H

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __cplusplus
static
#endif
inline uint32_t pal_execute_in_32_inline(uint16_t address)
{
    uint32_t value = 0;

    __asm__ __volatile__(
        "mov {%[addr], %%dx | dx, %[addr]};"
        "{inl %%dx, %[val] | in %[val], dx};"
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
