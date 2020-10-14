bits 64
default rel

section .text

global pal_execute_invd
pal_execute_invd :
    invd
    ret
