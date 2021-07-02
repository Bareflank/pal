bits 64
default rel

section .text

global pal_execute_vmcall_kvm
pal_execute_vmcall_kvm :
    mov rax, rdi
    mov rbx, rsi
    xchg rcx, rdx
    mov rsi, r8
    vmcall
    ret
