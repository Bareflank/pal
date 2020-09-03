.code

pal_execute_vmwrite proc
    vmwrite rcx, rdx;
    ret;
pal_execute_vmwrite endp

end
