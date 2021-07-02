bits 64
default rel

section .text

global pal_execute_hlt
pal_execute_hlt :
    hlt
