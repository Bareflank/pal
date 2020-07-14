.code

pal_execute_xgetbv proc
    ; The argument to pass to xgetbv via ecx is already
    ; there, since it is the first integer passed here.
    xgetbv;

    ; The result is stored in edx:eax, so get it into rax
    ; and return.
    shl rdx, 032;
    or rax, rdx;

    ret;

pal_execute_xgetbv endp

pal_execute_xsetbv proc
    ; The address is already loaded in rcx because
    ; it is the first integer argument. The value to
    ; write is in rdx. We need that to be in edx:eax.
    mov rax, rdx;
    shr rdx, 032;
    xsetbv;

    ret;

pal_execute_xsetbv endp

end
