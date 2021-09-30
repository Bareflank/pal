use pal;

pub unsafe fn run_example() {
    // Execute the Intel VMCALL instruction with no arguments
    pal::instruction::execute_vmcall();

    // Xen hypercall ABI using the Intel VMCALL instruction:
    let mut index = 0;     // rax
    let mut arg1 = 0;      // rdi
    let mut arg2 = 0;      // rsi
    let mut arg3 = 0;      // rdx
    let mut arg4 = 0;      // r10
    let arg5 = 0;      // r8
    let arg6 = 0;      // r9
    let mut _result = pal::instruction::execute_vmcall_xen(index, arg1, arg2, arg3, arg4, arg5, arg6);

    // KVM hypercall ABI using the Intel VMCALL instruction:
    index = 0;              // rax
    arg1 = 0;               // rbx
    arg2 = 0;               // rcx
    arg3 = 0;               // rdx
    arg4 = 0;               // rsi
    _result = pal::instruction::execute_vmcall_kvm(index, arg1, arg2, arg3, arg4);
}
