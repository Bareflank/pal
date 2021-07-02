bits 64
default rel

section .text

global pal_execute_bsr 
pal_execute_bsr :
    bsr rax, rdi
    ret
