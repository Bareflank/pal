bits 64
default rel

section .text

global vmptrst_x64_64bit_none_systemv 
vmptrst_x64_64bit_none_systemv :
    vmptrst [rdi]
    ret
