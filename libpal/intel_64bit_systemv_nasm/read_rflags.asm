bits 64
default rel

section .text

global pal_execute_read_rflags
pal_execute_read_rflags :
    pushfq
    pop rax
    ret
