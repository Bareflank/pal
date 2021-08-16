.code

; MS64 argument order: RCX, RDX, R8, R9, stack
; vmcall argument order: rax, rdi, rsi, rdx, r10, r8, r9
; vmcall clobbers: rax, rcx, rdx, rdi, rsi, r8, r9. r10, r11
pal_execute_vmcall_xen proc
    ; collect fifth and higher arguments from the stack
    pop r10;
    pop r8;
    pop r9;
    
    ; save callee-preserved (non-volatile) registers
    push rdi;
    push rsi;

    ; move register arguments into hypercall registers
    mov rax, rcx;
    mov rdi, rdx;
    mov rsi, r8;
    mov rdx, r9;

    vmcall;

    ; restore callee-preserved (non-volatile) registers
    pop rsi;
    pop rdi;

    ret;

pal_execute_vmcall_xen endp

end
