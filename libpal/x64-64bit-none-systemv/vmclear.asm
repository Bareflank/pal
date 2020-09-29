bits 64
default rel

section .text

global vmclear_x64_64bit_none_systemv 
vmclear_x64_64bit_none_systemv :
    vmclear [rdi]
    ret
