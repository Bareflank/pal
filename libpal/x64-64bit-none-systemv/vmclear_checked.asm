bits 64
default rel

section .text

global vmclear_checked_x64_64bit_none_systemv 
vmclear_checked_x64_64bit_none_systemv :
    vmclear [rdi]
    jbe _vmclear_checked_x64_64bit_none_systemv_failure
    mov rax, 0x1
    ret

_vmclear_checked_x64_64bit_none_systemv_failure:
    mov rax, 0x0
    ret
