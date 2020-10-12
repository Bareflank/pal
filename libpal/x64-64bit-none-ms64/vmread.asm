.code

vmread_x64_64bit_none_ms64 proc
   ; The VMCS address was given in rcx
   vmread rax, rcx;

   ret;

vmread_x64_64bit_none_ms64 endp

end
