bits 64
default rel

section .text

global write_rflags_x64_64bit_none_systemv 
write_rflags_x64_64bit_none_systemv :
    push rdi
    popf
    ret
