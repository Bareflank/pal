bits 64
default rel

section .text

global pal_execute_sidt
pal_execute_sidt :
    sidt [rdi]
    ret
