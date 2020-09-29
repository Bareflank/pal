bits 64
default rel

section .text

global write_cs_x64_64bit_none_systemv 
write_cs_x64_64bit_none_systemv :
    ; The added 0x48 is an undocumented issue with NASM. Basically, even though
    ; BITS 64 is used, and we are compiling for 64bit, NASM does not add the
    ; REX prefix to the retf instruction. As a result, we need to hand jam it
    ; in otherwise NASM will compile a 32bit instruction, and the data on the
    ; stack will be wrong
    pop rax
    push di
    push rax
    db 0x48
    retf
