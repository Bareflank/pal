bits 64
default rel

section .text

global pal_execute_mfence
pal_execute_mfence :
    mfence
    ret
