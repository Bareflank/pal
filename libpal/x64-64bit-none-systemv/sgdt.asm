bits 64
default rel

section .text

global sgdt_x64_64bit_none_systemv 
sgdt_x64_64bit_none_systemv :
    sgdt [rdi]
    ret
