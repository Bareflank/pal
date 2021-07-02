bits 64
default rel

section .text

global pal_execute_read_es
pal_execute_read_es :
    xor rax, rax
    mov ax, es
    ret
