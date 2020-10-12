bits 64
default rel

section .text

global write_es_x64_64bit_none_systemv 
write_es_x64_64bit_none_systemv :
    xor rax, rax
    mov es, di
    ret
