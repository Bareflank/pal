bits 64
default rel

section .text

global read_tr_x64_64bit_none_systemv 
read_tr_x64_64bit_none_systemv :
    xor rax, rax
    str ax
    ret
