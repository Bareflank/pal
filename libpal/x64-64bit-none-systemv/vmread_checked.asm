bits 64
default rel

section .text

global pal_execute_vmread_checked
pal_execute_vmread_checked :
    vmread [rsi], rdi
    jbe pal_execute_vmread_checked_failure
    mov rax, 0x1
    ret

pal_execute_vmread_checked_failure :
    mov rax, 0x0
    ret
