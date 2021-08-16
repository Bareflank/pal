.code

pal_execute_in_32 proc

    xor rax, rax;
    mov rdx, rcx;
    in eax, dx;

    ret;

pal_execute_in_32 endp

end
