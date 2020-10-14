bits 64
default rel

section .text

global pal_execute_sgdt
pal_execute_sgdt :
    sgdt [rdi]
    ret
