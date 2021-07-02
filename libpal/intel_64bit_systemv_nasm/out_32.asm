bits 64
default rel

section .text

global pal_execute_out_32
pal_execute_out_32 :
    mov rdx, rdi
    mov rax, rsi
    out dx, eax
    xor rax, rax    ; <-- TODO: Why is this needed here?
    ret
