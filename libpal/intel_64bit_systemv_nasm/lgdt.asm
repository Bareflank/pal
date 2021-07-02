bits 64
default rel

section .text

global pal_execute_lgdt
pal_execute_lgdt :
    lgdt [rdi]
    ret
