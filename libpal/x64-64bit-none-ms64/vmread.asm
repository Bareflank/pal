.code

pal_execute_vmread proc
   ; The VMCS address was given in rcx
   vmread rax, rcx;

   ret;

pal_execute_vmread endp

end
