#ifndef PAL_EXECUTE_WRITE_CR0_INLINE_H
#define PAL_EXECUTE_WRITE_CR0_INLINE_H

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __cplusplus
static
#endif
inline void pal_execute_write_cr0_inline(uint64_t value)
{
    __asm__ __volatile__(
        "mov {%[v], %%cr0 | cr0, %[v]};"
        : 
        : [v] "r"(value)
        : 
    );
}

#ifdef __cplusplus
}
#endif

#endif
