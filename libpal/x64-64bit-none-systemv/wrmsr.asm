bits 64
default rel

section .text

global wrmsr_x64_64bit_none_systemv 
wrmsr_x64_64bit_none_systemv :
    mov rax, rsi
    mov rdx, rsi
    shr rdx, 32
    mov rcx, rdi
    wrmsr
    ret
