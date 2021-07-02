bits 64
default rel

section .text

global pal_execute_write_es
pal_execute_write_es :
    xor rax, rax
    mov es, di
    ret
