bits 64
default rel

section .text

global pal_execute_rdmsr 
pal_execute_rdmsr :
    mov rcx, rdi
    rdmsr
    shl rdx, 32
    or rax, rdx
    ret
