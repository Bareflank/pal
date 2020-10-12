bits 64
default rel

section .text

global invvpid_checked_x64_64bit_none_systemv 
invvpid_checked_x64_64bit_none_systemv :
    invvpid rdi, [rsi]
    jbe _invvpid_checked_x64_64bit_none_systemv_failure
    mov rax, 0x1
    ret

_invvpid_checked_x64_64bit_none_systemv_failure:
    mov rax, 0x0
    ret
