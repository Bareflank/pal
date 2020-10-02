bits 64
default rel

section .text

global vmptrst_checked_x64_64bit_none_systemv 
vmptrst_checked_x64_64bit_none_systemv :
    vmptrst [rdi]
    jbe _vmptrst_checked_x64_64bit_none_systemv_failure
    mov rax, 0x1
    ret

_vmptrst_checked_x64_64bit_none_systemv_failure:
    mov rax, 0x0
    ret
