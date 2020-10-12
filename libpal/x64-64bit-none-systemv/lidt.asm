bits 64
default rel

section .text

global lidt_x64_64bit_none_systemv 
lidt_x64_64bit_none_systemv :
    lidt [rdi]
    ret
