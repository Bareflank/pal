bits 64
default rel

section .text

global invept_checked_x64_64bit_none_systemv 
invept_checked_x64_64bit_none_systemv :
    invept rdi, [rsi]
    jbe _invept_checked_x64_64bit_none_systemv_failure
    mov rax, 0x1
    ret

_invept_checked_x64_64bit_none_systemv_failure:
    mov rax, 0x0
    ret
