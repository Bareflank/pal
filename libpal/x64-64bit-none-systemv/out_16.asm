bits 64
default rel

section .text

global out_16_x64_64bit_none_systemv 
out_16_x64_64bit_none_systemv :
    mov rdx, rdi
    mov rax, rsi
    out dx, ax
    xor rax, rax    ; <-- TODO: Why is this needed here?
    ret
