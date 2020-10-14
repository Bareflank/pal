bits 64
default rel

section .text

global pal_execute_read_cr0 
pal_execute_read_cr0 :
    mov rax, cr0
    ret
