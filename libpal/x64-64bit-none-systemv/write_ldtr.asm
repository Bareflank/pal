bits 64
default rel

section .text

global pal_execute_write_ldtr
pal_execute_write_ldtr :
    lldt di
    ret
