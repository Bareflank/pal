#ifndef PAL_EXECUTE_VMCALL_INLINE_H
#define PAL_EXECUTE_VMCALL_INLINE_H

#ifdef __cplusplus
extern "C" {
#endif

#ifndef __cplusplus
static
#endif
void pal_execute_vmcall_inline(void)
{
    __asm__ __volatile__(
        "vmcall;"
        :
        :
        :
    );
}

#ifdef __cplusplus
}
#endif

#endif
