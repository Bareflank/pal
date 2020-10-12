bits 64
default rel

section .text

global write_tr_x64_64bit_none_systemv 
write_tr_x64_64bit_none_systemv :
    ltr di
    ret
