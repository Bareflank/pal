bits 64
default rel

section .text

global pal_execute_read_tr
pal_execute_read_tr :
    xor rax, rax
    str ax
    ret
