bits 64
default rel

section .text

global write_cr8_x64_64bit_none_systemv 
write_cr8_x64_64bit_none_systemv :
    mov cr8, rdi
    ret
