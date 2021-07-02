bits 64
default rel

section .text

global pal_execute_xsetbv 
pal_execute_xsetbv :
    mov rax, rdi
    mov rdx, rdi
    shr rdx, 32
    mov rcx, 0
    xsetbv
    ret
