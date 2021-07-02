.code

pal_execute_write_cr3 proc
    mov cr3, rcx;
    ret;
pal_execute_write_cr3 endp

end
