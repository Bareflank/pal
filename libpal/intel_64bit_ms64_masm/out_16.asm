.code

pal_execute_out_16 proc
    mov rax, rdx;
    mov rdx, rcx;
    out dx, ax;
    ret;

pal_execute_out_16 endp

end
