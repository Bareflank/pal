bits 64
default rel

section .text

global vmxoff_checked_x64_64bit_none_systemv 
vmxoff_checked_x64_64bit_none_systemv :
    vmxoff
    jbe _vmxoff_checked_x64_64bit_none_systemv_failure
    mov rax, 0x1
    ret

_vmxoff_checked_x64_64bit_none_systemv_failure:
    mov rax, 0x0
    ret
