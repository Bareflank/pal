bits 64
default rel

section .text

global pal_execute_write_cr2 
pal_execute_write_cr2 :
    mov cr2, rdi
    ret
