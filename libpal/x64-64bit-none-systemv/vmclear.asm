bits 64
default rel

section .text

global pal_execute_vmclear
pal_execute_vmclear :
    vmclear [rdi]
    ret
