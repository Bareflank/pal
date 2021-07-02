bits 64
default rel

section .text

global pal_execute_popcnt
pal_execute_popcnt :
    popcnt rax, rdi
    ret
