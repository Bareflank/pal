bits 64
default rel

section .text

global pal_execute_read_fs
pal_execute_read_fs :
    xor rax, rax
    mov ax, fs
    ret
