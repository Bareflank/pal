#ifndef PAL_EXECUTE_READ_CR3_INLINE_H
#define PAL_EXECUTE_READ_CR3_INLINE_H

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __cplusplus
static
#endif
inline uint64_t pal_execute_read_cr3_inline(void)
{
    uint64_t value = 0;
    __asm__ __volatile__(
        "mov {%%cr3, %[v] | %[v], cr3};"
        : [v] "=r"(value)
        : 
        : 
    );
    return value;
}

#ifdef __cplusplus
}
#endif

#endif
