bits 64
default rel

section .text

global xsetbv_x64_64bit_none_systemv 
xsetbv_x64_64bit_none_systemv :
    mov rax, rdi
    mov rdx, rdi
    shr rdx, 32
    mov rcx, 0
    xsetbv
    ret
