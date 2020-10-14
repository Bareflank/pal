bits 64
default rel

section .text

global pal_execute_read_ldtr
pal_execute_read_ldtr :
    xor rax, rax
    sldt ax
    ret
