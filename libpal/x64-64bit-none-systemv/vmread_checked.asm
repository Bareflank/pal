bits 64
default rel

section .text

global vmread_checked_x64_64bit_none_systemv 
vmread_checked_x64_64bit_none_systemv :
    vmread [rsi], rdi
    jbe _vmread_checked_x64_64bit_none_systemv_failure
    mov rax, 0x1
    ret

_vmread_checked_x64_64bit_none_systemv_failure:
    mov rax, 0x0
    ret
