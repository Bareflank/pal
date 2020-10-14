bits 64
default rel

section .text

global pal_execute_invvpid
pal_execute_invvpid :
    invvpid rdi, [rsi]
    ret
