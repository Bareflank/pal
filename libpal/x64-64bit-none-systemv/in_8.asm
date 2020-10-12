bits 64
default rel

section .text

global in_8_x64_64bit_none_systemv 
in_8_x64_64bit_none_systemv :
    xor rax, rax
    mov rdx, rdi
    in al, dx
    ret
