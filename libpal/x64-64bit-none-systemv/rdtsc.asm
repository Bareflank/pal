bits 64
default rel

section .text

global rdtsc_x64_64bit_none_systemv 
rdtsc_x64_64bit_none_systemv :
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
