bits 64
default rel

section .text

global pal_execute_vmptrld
pal_execute_vmptrld :
    vmptrld [rdi]
    ret
