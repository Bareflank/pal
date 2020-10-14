bits 64
default rel

section .text

global pal_execute_out_8
pal_execute_out_8 :
    mov rdx, rdi
    mov rax, rsi
    out dx, al
    xor rax, rax    ; <-- TODO: Why is this needed here?
    ret
