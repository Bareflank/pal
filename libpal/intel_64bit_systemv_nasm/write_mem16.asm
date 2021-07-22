bits 64
default rel

section .text

global pal_execute_write_mem16 
pal_execute_write_mem16 :
    mov WORD [rdi], si 
    ret
