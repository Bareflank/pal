bits 64
default rel

section .text

global pal_execute_invlpg
pal_execute_invlpg :
    invlpg [rdi]
    ret
