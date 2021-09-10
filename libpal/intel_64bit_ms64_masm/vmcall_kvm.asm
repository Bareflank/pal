.code

; MS64 argument order: RCX, RDX, R8, R9, stack
; vmcall argument order: rax, rbx, rcx, rdx, rsi
; vmcall clobbers: rax (TODO: other registers may be clobbered if specifically documented)
pal_execute_vmcall_kvm proc
    ; collect fifth and higher arguments from the stack
    pop r10;
    
    ; save callee-preserved (non-volatile) registers
    push rbx;
    push rsi;

    mov rax, rcx;
    mov rbx, rdx;
    mov rcx, r8;
    mov rdx, r9;
    mov rsi, r10;

    vmcall;

    ; restore callee-preserved (non-volatile) registers
    pop rsi;
    pop rbx;

    ret;

pal_execute_vmcall_kvm endp

end
