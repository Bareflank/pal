bits 64
default rel

section .text

global vmptrld_x64_64bit_none_systemv 
vmptrld_x64_64bit_none_systemv :
    vmptrld [rdi]
    ret
