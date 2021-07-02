bits 64
default rel

section .text

global pal_execute_lfence
pal_execute_lfence :
    lfence
    ret
