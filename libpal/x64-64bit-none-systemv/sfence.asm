bits 64
default rel

section .text

global pal_execute_sfence
pal_execute_sfence :
    sfence
    ret
