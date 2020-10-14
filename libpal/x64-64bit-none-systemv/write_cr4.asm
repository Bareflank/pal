bits 64
default rel

section .text

global pal_execute_write_cr4 
pal_execute_write_cr4 :
    mov cr4, rdi
    ret
