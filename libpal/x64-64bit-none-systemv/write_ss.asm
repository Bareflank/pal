bits 64
default rel

section .text

global pal_execute_write_ss
pal_execute_write_ss :
    mov ss, di
    ret
