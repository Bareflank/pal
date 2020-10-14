bits 64
default rel

section .text

global pal_execute_in_32 
pal_execute_in_32 :
    xor rax, rax
    mov rdx, rdi
    in eax, dx
    ret
