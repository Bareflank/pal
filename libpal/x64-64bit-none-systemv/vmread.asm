bits 64
default rel

section .text

global vmread_x64_64bit_none_systemv 
vmread_x64_64bit_none_systemv :
    vmread [rsi], rdi
    ret
