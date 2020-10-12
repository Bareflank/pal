bits 64
default rel

section .text

global write_gs_x64_64bit_none_systemv 
write_gs_x64_64bit_none_systemv :
    mov gs, di
    ret
