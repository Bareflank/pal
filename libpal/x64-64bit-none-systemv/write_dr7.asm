bits 64
default rel

section .text

global write_dr7_x64_64bit_none_systemv 
write_dr7_x64_64bit_none_systemv :
    mov dr7, rdi
    ret
