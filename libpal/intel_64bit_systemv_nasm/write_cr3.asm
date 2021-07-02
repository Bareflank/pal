bits 64
default rel

section .text

global pal_execute_write_cr3 
pal_execute_write_cr3 :
    mov cr3, rdi
    ret
