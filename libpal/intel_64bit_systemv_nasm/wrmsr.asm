bits 64
default rel

section .text

global pal_execute_wrmsr 
pal_execute_wrmsr :
    mov rax, rsi
    mov rdx, rsi
    shr rdx, 32
    mov rcx, rdi
    wrmsr
    ret
