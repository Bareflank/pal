.code

; The C function signature looks like:
;     pal_cpuid_register_values pal_execute_cpuid(uint32_t,uint32_t)
; where pal_cpuid_register_values is 16 bytes (4 32-bit integers).
;
; A struct pointer is given in rcx. The first and second integer
; arguments are passed into rdx and r8, respectively.
cpuid_x64_64bit_none_ms64  proc
	push rcx;

	mov eax, edx;
	mov ecx, r8d;
	cpuid;

	pop r8;

	mov [r8], eax
	mov [r8+4], ebx;
	mov [r8+8], ecx;
	mov [r8+12], edx;

	mov rax, r8;

	ret;

cpuid_x64_64bit_none_ms64  endp

end
