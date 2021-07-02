bits 64
default rel

section .text

global pal_execute_read_ss
pal_execute_read_ss :
    xor rax, rax
    mov ax, ss
    ret
