bits 64
default rel

section .text

global pal_execute_write_cr8 
pal_execute_write_cr8 :
    mov cr8, rdi
    ret
