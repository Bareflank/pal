bits 64
default rel

section .text

global bsf_x64_64bit_none_systemv 
bsf_x64_64bit_none_systemv :
    bsf rax, rdi
    ret
