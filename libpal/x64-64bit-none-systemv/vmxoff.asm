bits 64
default rel

section .text

global vmxoff_x64_64bit_none_systemv 
vmxoff_x64_64bit_none_systemv :
    vmxoff
    ret
