bits 64
default rel

section .text

global pal_execute_xgetbv 
pal_execute_xgetbv :
    mov rcx, 0
    xgetbv
    shl rdx, 32
    or rax, rdx
    ret
