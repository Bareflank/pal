bits 64
default rel

section .text

global read_dr7_x64_64bit_none_systemv 
read_dr7_x64_64bit_none_systemv :
    mov rax, dr7
    ret
