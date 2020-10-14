bits 64
default rel

section .text

global pal_execute_read_cr3 
pal_execute_read_cr3 :
    mov rax, cr3
    ret
