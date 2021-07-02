bits 64
default rel

section .text

global pal_execute_read_cr4 
pal_execute_read_cr4 :
    mov rax, cr4
    ret
