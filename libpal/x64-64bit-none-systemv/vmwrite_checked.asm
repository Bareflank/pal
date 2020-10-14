bits 64
default rel

section .text

global pal_execute_vmwrite_checked
pal_execute_vmwrite_checked :
    vmwrite rdi, rsi
    jbe pal_execute_vmwrite_checked_failure
    mov rax, 0x1
    ret

pal_execute_vmwrite_checked_failure :
    mov rax, 0x0
    ret
