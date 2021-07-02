bits 64
default rel

section .text

global pal_execute_vmxon
pal_execute_vmxon :
    vmxon [rdi]
    ret
