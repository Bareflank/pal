bits 64
default rel

section .text

global rdtscp_x64_64bit_none_systemv 
rdtscp_x64_64bit_none_systemv :
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
