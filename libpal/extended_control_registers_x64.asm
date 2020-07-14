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

end
