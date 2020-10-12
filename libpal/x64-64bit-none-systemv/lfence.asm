bits 64
default rel

section .text

global lfence_x64_64bit_none_systemv 
lfence_x64_64bit_none_systemv :
    lfence
    ret
