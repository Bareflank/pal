bits 64
default rel

section .text

global pal_execute_read_mem16 
pal_execute_read_mem16 :
    mov ax, WORD [rdi]
    ret
