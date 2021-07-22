bits 64
default rel

section .text

global pal_execute_write_mem64 
pal_execute_write_mem64 :
    mov QWORD [rdi], rsi 
    ret
