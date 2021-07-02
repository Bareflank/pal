bits 64
default rel

section .text

global pal_execute_vmxoff
pal_execute_vmxoff :
    vmxoff
    ret
