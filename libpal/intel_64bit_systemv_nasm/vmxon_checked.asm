bits 64
default rel

section .text

global pal_execute_vmxon_checked
pal_execute_vmxon_checked :
    vmxon [rdi]
    jbe pal_execute_vmxon_checked_failure
    mov rax, 0x1
    ret

pal_execute_vmxon_checked_failure :
    mov rax, 0x0
    ret
