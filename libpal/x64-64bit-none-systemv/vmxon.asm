bits 64
default rel

section .text

global vmxon_x64_64bit_none_systemv 
vmxon_x64_64bit_none_systemv :
    vmxon [rdi]
    ret
