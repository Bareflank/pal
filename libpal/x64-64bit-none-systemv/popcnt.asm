bits 64
default rel

section .text

global popcnt_x64_64bit_none_systemv 
popcnt_x64_64bit_none_systemv :
    popcnt rax, rdi
    ret
