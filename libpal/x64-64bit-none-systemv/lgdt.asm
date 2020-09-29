bits 64
default rel

section .text

global lgdt_x64_64bit_none_systemv 
lgdt_x64_64bit_none_systemv :
    lgdt [rdi]
    ret
