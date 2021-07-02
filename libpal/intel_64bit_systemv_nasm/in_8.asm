bits 64
default rel

section .text

global pal_execute_in_8
pal_execute_in_8 :
    xor rax, rax
    mov rdx, rdi
    in al, dx
    ret
