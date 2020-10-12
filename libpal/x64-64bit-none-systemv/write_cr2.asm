bits 64
default rel

section .text

global write_cr2_x64_64bit_none_systemv 
write_cr2_x64_64bit_none_systemv :
    mov cr2, rdi
    ret
