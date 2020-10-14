bits 64
default rel

section .text

global pal_execute_vmread 
pal_execute_vmread :
    vmread [rsi], rdi
    ret
