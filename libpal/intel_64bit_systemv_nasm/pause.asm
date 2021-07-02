bits 64
default rel

section .text

global pal_execute_pause
pal_execute_pause :
    pause
    ret
