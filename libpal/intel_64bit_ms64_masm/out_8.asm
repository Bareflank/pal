.code

pal_execute_out_8 proc
    mov rax, rdx;
    mov rdx, rcx;
    out dx, al;
    ret;

pal_execute_out_8 endp

end
