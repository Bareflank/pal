bits 64
default rel

section .text

global pal_execute_vmptrst
pal_execute_vmptrst :
    vmptrst [rdi]
    ret
