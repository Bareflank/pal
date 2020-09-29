bits 64
default rel

section .text

global vmwrite_x64_64bit_none_systemv 
vmwrite_x64_64bit_none_systemv :
    vmwrite rdi, rsi
    ret
