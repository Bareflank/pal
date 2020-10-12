bits 64
default rel

section .text

global read_fs_x64_64bit_none_systemv 
read_fs_x64_64bit_none_systemv :
    xor rax, rax
    mov ax, fs
    ret
