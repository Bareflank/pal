bits 64
default rel

section .text

global xgetbv_x64_64bit_none_systemv 
xgetbv_x64_64bit_none_systemv :
    mov rcx, 0
    xgetbv
    shl rdx, 32
    or rax, rdx
    ret
