bits 64
default rel

section .text

global pal_execute_rdtsc
pal_execute_rdtsc :
    push rbx

    xor rax, rax
    xor rbx, rbx
    xor rcx, rcx
    xor rdx, rdx
    cpuid

    rdtsc
    shl rdx, 32
    or rax, rdx

    pop rbx
    ret
