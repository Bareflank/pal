bits 64
default rel

section .text

global pal_execute_read_mem64 
pal_execute_read_mem64 :
    mov rax, QWORD [rdi]
    ret
