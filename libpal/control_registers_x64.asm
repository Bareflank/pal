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

pal_execute_cr0_write proc
    mov cr0, rcx;
    ret;
pal_execute_cr0_write endp

pal_execute_cr2_write proc
    mov cr2, rcx;
    ret;
pal_execute_cr2_write endp

pal_execute_cr3_write proc
    mov cr3, rcx;
    ret;
pal_execute_cr3_write endp

pal_execute_cr4_write proc
    mov cr4, rcx;
    ret;
pal_execute_cr4_write endp

pal_execute_cr8_write proc
    mov cr8, rcx;
    ret;
pal_execute_cr8_write endp

end
