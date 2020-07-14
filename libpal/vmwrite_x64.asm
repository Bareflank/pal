.code

pal_execute_vmwrite proc
    vmwrite rdx, rcx;
    ret;
pal_execute_vmwrite endp

end
