bits 64
default rel

section .text

global pal_execute_vmxoff_checked
pal_execute_vmxoff_checked :
    vmxoff
    jbe pal_execute_vmxoff_checked_failure
    mov rax, 0x1
    ret

pal_execute_vmxoff_checked_failure :
    mov rax, 0x0
    ret
