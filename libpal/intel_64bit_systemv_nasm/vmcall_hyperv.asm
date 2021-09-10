bits 64
default rel

section .text

global pal_execute_vmcall_hyperv
pal_execute_vmcall_hyperv :
    mov rcx, rdi
    mov rdx, rsi

    vmcall

    mov rax, r8
    ret
