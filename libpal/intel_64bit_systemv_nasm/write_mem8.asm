bits 64
default rel

section .text

global pal_execute_write_mem8 
pal_execute_write_mem8 :
    mov BYTE [rdi], sil 
    ret
