bits 64
default rel

section .text

global pal_execute_vmclear_checked
pal_execute_vmclear_checked :
    vmclear [rdi]
    jbe pal_execute_vmclear_checked_failure
    mov rax, 0x1
    ret

pal_execute_vmclear_checked_failure :
    mov rax, 0x0
    ret
