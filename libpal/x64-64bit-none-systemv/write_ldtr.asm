bits 64
default rel

section .text

global write_ldtr_x64_64bit_none_systemv 
write_ldtr_x64_64bit_none_systemv :
    lldt di
    ret
