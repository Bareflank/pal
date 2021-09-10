.code

pal_execute_vmcall_hyperv proc

    vmcall;
    mov rax, r8;
    ret;

pal_execute_vmcall_hyperv endp

end
