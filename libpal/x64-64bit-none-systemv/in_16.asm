bits 64
default rel

section .text

global pal_execute_in_16 
pal_execute_in_16 :
    xor rax, rax
    mov rdx, rdi
    in ax, dx
    ret
