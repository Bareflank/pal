bits 64
default rel

section .text

global vmxon_checked_x64_64bit_none_systemv 
vmxon_checked_x64_64bit_none_systemv :
    vmxon [rdi]
    jbe _vmxon_checked_x64_64bit_none_systemv_failure
    mov rax, 0x1
    ret

_vmxon_checked_x64_64bit_none_systemv_failure:
    mov rax, 0x0
    ret
