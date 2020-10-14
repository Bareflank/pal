.code

pal_execute_cpuid proc
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

pal_execute_cpuid endp

end
