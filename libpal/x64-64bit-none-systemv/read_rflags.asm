bits 64
default rel

section .text

global read_rflags_x64_64bit_none_systemv 
read_rflags_x64_64bit_none_systemv :
    pushfq
    pop rax
    ret
