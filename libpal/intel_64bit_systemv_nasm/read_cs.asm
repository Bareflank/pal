bits 64
default rel

section .text

global pal_execute_read_cs
pal_execute_read_cs :
    xor rax, rax
    mov ax, cs
    ret
