bits 64
default rel

section .text

global read_cr8_x64_64bit_none_systemv 
read_cr8_x64_64bit_none_systemv :
    mov rax, cr8
    ret
