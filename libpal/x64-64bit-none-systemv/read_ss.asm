bits 64
default rel

section .text

global read_ss_x64_64bit_none_systemv 
read_ss_x64_64bit_none_systemv :
    xor rax, rax
    mov ax, ss
    ret
