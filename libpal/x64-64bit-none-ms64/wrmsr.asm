.code

wrmsr_x64_64bit_none_ms64  proc
    ; The address is already loaded in rcx because
    ; it is the first integer argument. The value to
    ; write is in rdx. We need that to be in edx:eax.
    mov rax, rdx;
    shr rdx, 032;
    wrmsr;

    ret;

wrmsr_x64_64bit_none_ms64  endp

end
