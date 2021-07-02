bits 64
default rel

section .text

global pal_execute_write_rflags
pal_execute_write_rflags :
    push rdi
    popf
    ret
