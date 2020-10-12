bits 64
default rel

section .text

global vmwrite_checked_x64_64bit_none_systemv 
vmwrite_checked_x64_64bit_none_systemv :
    vmwrite rdi, rsi
    jbe _vmwrite_checked_x64_64bit_none_systemv_failure
    mov rax, 0x1
    ret

_vmwrite_checked_x64_64bit_none_systemv_failure:
    mov rax, 0x0
    ret
