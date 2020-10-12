bits 64
default rel

section .text

global wbinvd_x64_64bit_none_systemv 
wbinvd_x64_64bit_none_systemv :
    wbinvd
    ret
