.code

pal_execute_out_32 proc
    mov rax, rdx;
    mov rdx, rcx;
    out dx, eax;
    ret;

pal_execute_out_32 endp

end
