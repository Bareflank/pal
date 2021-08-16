.code

pal_execute_in_16 proc

    xor rax, rax;
    mov rdx, rcx;
    in ax, dx;

    ret;

pal_execute_in_16 endp

end
