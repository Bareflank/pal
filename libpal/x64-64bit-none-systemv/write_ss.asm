bits 64
default rel

section .text

global write_ss_x64_64bit_none_systemv 
write_ss_x64_64bit_none_systemv :
    mov ss, di
    ret
