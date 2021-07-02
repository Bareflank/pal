bits 64
default rel

section .text

global pal_execute_vmwrite 
pal_execute_vmwrite :
    vmwrite rdi, rsi
    ret
