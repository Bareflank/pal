bits 64
default rel

section .text

global pal_execute_vmread 
pal_execute_vmread :
    vmread rax, rdi
    ret
