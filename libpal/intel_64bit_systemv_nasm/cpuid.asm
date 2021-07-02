bits 64
default rel

section .text

global pal_execute_cpuid 
pal_execute_cpuid :
    mov rax, rdi
    mov rcx, rsi

    cpuid

    ; The systemv ABI specificies that return values equal or smaller than
    ; "two eight-bytes" in size are returned through registers rax and rdx:
    shl rbx, 32
    shl rdx, 32
    or rax, rbx
    or rdx, rcx

    ret
