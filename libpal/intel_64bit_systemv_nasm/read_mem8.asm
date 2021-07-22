bits 64
default rel

section .text

global pal_execute_read_mem8 
pal_execute_read_mem8 :
    mov al, BYTE [rdi]
    ret
