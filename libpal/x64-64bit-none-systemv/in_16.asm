bits 64
default rel

section .text

global in_16_x64_64bit_none_systemv 
in_16_x64_64bit_none_systemv :
    xor rax, rax
    mov rdx, rdi
    in ax, dx
    ret
