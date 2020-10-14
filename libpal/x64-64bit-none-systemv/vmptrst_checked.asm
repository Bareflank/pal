bits 64
default rel

section .text

global pal_execute_vmptrst_checked
pal_execute_vmptrst_checked :
    vmptrst [rdi]
    jbe pal_execute_vmptrst_checked_failure
    mov rax, 0x1
    ret

pal_execute_vmptrst_checked_failure :
    mov rax, 0x0
    ret
