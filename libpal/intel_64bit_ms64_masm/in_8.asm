.code

pal_execute_in_8 proc

    xor rax, rax;
    mov rdx, rcx;
    in al, dx;

    ret;

pal_execute_in_8 endp

end
