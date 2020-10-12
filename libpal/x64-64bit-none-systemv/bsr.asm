bits 64
default rel

section .text

global bsr_x64_64bit_none_systemv 
bsr_x64_64bit_none_systemv :
    bsr rax, rdi
    ret
