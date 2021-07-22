bits 64
default rel

section .text

global pal_execute_read_mem32 
pal_execute_read_mem32 :
    mov eax, DWORD [rdi]
    ret
