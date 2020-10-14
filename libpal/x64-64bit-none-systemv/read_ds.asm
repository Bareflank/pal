bits 64
default rel

section .text

global pal_execute_read_ds
pal_execute_read_ds :
    xor rax, rax
    mov ax, ds
    ret
