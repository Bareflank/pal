bits 64
default rel

section .text

global pal_execute_write_ds
pal_execute_write_ds :
    mov ds, di
    ret
