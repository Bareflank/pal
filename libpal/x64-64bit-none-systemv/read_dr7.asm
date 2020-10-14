bits 64
default rel

section .text

global pal_execute_read_dr7
pal_execute_read_dr7 :
    mov rax, dr7
    ret
