bits 64
default rel

section .text

global write_cr0_x64_64bit_none_systemv 
write_cr0_x64_64bit_none_systemv :
    mov cr0, rdi
    ret
