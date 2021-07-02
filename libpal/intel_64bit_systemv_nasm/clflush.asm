bits 64
default rel

section .text

global pal_execute_clflush
pal_execute_clflush :
    clflush [rdi]
    ret
