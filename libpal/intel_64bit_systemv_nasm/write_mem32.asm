bits 64
default rel

section .text

global pal_execute_write_mem32 
pal_execute_write_mem32 :
    mov DWORD [rdi], esi 
    ret
