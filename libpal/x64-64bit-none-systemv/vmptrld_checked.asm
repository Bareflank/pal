bits 64
default rel

section .text

global vmptrld_checked_x64_64bit_none_systemv 
vmptrld_checked_x64_64bit_none_systemv :
    vmptrld [rdi]
    jbe _vmptrld_checked_x64_64bit_none_systemv_failure
    mov rax, 0x1
    ret

_vmptrld_checked_x64_64bit_none_systemv_failure:
    mov rax, 0x0
    ret
