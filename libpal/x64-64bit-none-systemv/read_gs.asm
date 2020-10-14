bits 64
default rel

section .text

global pal_execute_read_gs
pal_execute_read_gs :
    xor rax, rax
    mov ax, gs
    ret
