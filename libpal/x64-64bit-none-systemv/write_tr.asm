bits 64
default rel

section .text

global pal_execute_write_tr
pal_execute_write_tr :
    ltr di
    ret
