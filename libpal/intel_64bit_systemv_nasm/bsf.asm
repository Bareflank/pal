bits 64
default rel

section .text

global pal_execute_bsf 
pal_execute_bsf :
    bsf rax, rdi
    ret
