.code

pal_execute_rdmsr proc
    ; The argument to pass to rdmsr via ecx is already
    ; there, since it is the first integer passed here.
    rdmsr;

    ; The result is stored in edx:eax, so get it into rax
    ; and return.
    shl rdx, 032;
    or rax, rdx;

    ret;

pal_execute_rdmsr endp

end
