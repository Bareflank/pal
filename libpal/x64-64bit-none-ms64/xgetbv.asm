.code

xgetbv_x64_64bit_none_ms64 proc
    ; The argument to pass to xgetbv via ecx is already
    ; there, since it is the first integer passed here.
    xgetbv;

    ; The result is stored in edx:eax, so get it into rax
    ; and return.
    shl rdx, 032;
    or rax, rdx;

    ret;

xgetbv_x64_64bit_none_ms64 endp

end
