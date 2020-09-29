bits 64
default rel

section .text

global write_fs_x64_64bit_none_systemv 
write_fs_x64_64bit_none_systemv :
    mov fs, di
    ret
