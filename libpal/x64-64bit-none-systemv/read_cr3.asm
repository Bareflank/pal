bits 64
default rel

section .text

global read_cr3_x64_64bit_none_systemv 
read_cr3_x64_64bit_none_systemv :
    mov rax, cr3
    ret
