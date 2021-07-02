bits 64
default rel

section .text

global pal_execute_vmcall_xen
pal_execute_vmcall_xen :
    mov rax, rdi
    mov rdi, rsi
    mov rsi, rdx
    mov rdx, rcx
    mov r10, r8
    mov r8, r9
    pop r9
    vmcall
    ret
