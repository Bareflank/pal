bits 64
default rel

section .text

global invd_x64_64bit_none_systemv 
invd_x64_64bit_none_systemv :
    invd
    ret
