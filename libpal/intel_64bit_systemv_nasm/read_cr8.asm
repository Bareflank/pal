bits 64
default rel

section .text

global pal_execute_read_cr8 
pal_execute_read_cr8 :
    mov rax, cr8
    ret
