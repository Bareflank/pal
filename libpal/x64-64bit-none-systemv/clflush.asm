bits 64
default rel

section .text

global clflush_x64_64bit_none_systemv
clflush_x64_64bit_none_systemv :
    clflush [rdi]
    ret
