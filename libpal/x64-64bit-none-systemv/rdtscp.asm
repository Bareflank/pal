bits 64
default rel

section .text

global pal_execute_rdtscp
pal_execute_rdtscp :
    push rbx

    rdtscp
    shl rdx, 32
    or rax, rdx

    mov rdi, rax

    xor rax, rax
    xor rbx, rbx
    xor rcx, rcx
    xor rdx, rdx
    cpuid

    mov rax, rdi

    pop rbx
    ret
