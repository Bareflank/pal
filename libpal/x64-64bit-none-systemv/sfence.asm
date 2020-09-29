bits 64
default rel

section .text

global sfence_x64_64bit_none_systemv 
sfence_x64_64bit_none_systemv :
    sfence
    ret
