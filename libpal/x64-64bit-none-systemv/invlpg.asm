bits 64
default rel

section .text

global invlpg_x64_64bit_none_systemv
invlpg_x64_64bit_none_systemv :
    invlpg [rdi]
    ret
