bits 64
default rel

section .text

global pal_execute_write_gs
pal_execute_write_gs :
    mov gs, di
    ret
