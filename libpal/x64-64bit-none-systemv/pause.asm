bits 64
default rel

section .text

global pause_x64_64bit_none_systemv 
pause_x64_64bit_none_systemv :
    pause
    ret
