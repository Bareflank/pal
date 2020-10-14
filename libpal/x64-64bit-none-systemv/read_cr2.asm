bits 64
default rel

section .text

global pal_execute_read_cr2 
pal_execute_read_cr2 :
    mov rax, cr2
    ret
