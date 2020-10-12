bits 64
default rel

section .text

global read_cr2_x64_64bit_none_systemv 
read_cr2_x64_64bit_none_systemv :
    mov rax, cr2
    ret
