bits 64
default rel

section .text

global pal_execute_wbinvd
pal_execute_wbinvd :
    wbinvd
    ret
