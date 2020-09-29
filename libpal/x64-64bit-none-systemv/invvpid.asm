bits 64
default rel

section .text

global invvpid_x64_64bit_none_systemv
invvpid_x64_64bit_none_systemv :
    invvpid rdi, [rsi]
    ret
