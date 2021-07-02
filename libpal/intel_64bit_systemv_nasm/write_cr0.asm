bits 64
default rel

section .text

global pal_execute_write_cr0 
pal_execute_write_cr0 :
    mov cr0, rdi
    ret
