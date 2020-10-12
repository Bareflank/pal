bits 64
default rel

section .text

global sidt_x64_64bit_none_systemv 
sidt_x64_64bit_none_systemv :
    sidt [rdi]
    ret
