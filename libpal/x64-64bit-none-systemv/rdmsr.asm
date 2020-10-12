bits 64
default rel

section .text

global rdmsr_x64_64bit_none_systemv 
rdmsr_x64_64bit_none_systemv :
    mov rcx, rdi
    rdmsr
    shl rdx, 32
    or rax, rdx
    ret
