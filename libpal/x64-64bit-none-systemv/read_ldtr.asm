bits 64
default rel

section .text

global read_ldtr_x64_64bit_none_systemv 
read_ldtr_x64_64bit_none_systemv :
    xor rax, rax
    sldt ax
    ret
