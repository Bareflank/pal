bits 64
default rel

section .text

global pal_execute_out_16
pal_execute_out_16 :
    mov rdx, rdi
    mov rax, rsi
    out dx, ax
    xor rax, rax    ; <-- TODO: Why is this needed here?
    ret
