bits 64
default rel

section .text

global write_cr3_x64_64bit_none_systemv 
write_cr3_x64_64bit_none_systemv :
    mov cr3, rdi
    ret
