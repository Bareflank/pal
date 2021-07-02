bits 64
default rel

section .text

global pal_execute_write_fs
pal_execute_write_fs :
    mov fs, di
    ret
