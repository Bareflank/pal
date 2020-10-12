bits 64
default rel

section .text

global write_ds_x64_64bit_none_systemv 
write_ds_x64_64bit_none_systemv :
    mov ds, di
    ret
