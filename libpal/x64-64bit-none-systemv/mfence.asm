bits 64
default rel

section .text

global mfence_x64_64bit_none_systemv 
mfence_x64_64bit_none_systemv :
    mfence
    ret
