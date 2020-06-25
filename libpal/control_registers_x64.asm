.code

pal_execute_cr0_read proc
    mov rax, cr0;
    ret;
pal_execute_cr0_read endp

pal_execute_cr2_read proc
    mov rax, cr2;
    ret;
pal_execute_cr2_read endp

pal_execute_cr3_read proc
    mov rax, cr3;
    ret;
pal_execute_cr3_read endp

pal_execute_cr4_read proc
    mov rax, cr4;
    ret;
pal_execute_cr4_read endp

pal_execute_cr8_read proc
    mov rax, cr8;
    ret;
pal_execute_cr8_read endp

end
