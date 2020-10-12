bits 64
default rel

section .text

global invept_x64_64bit_none_systemv
invept_x64_64bit_none_systemv :
    invept rdi, [rsi]
    ret
