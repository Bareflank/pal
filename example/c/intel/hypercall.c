#include "pal/instruction/vmcall.h"
#include "pal/instruction/vmcall_hyperv.h"
#include "pal/instruction/vmcall_kvm.h"
#include "pal/instruction/vmcall_xen.h"

int main(void)
{
    // Execute the Intel VMCALL instruction with no arguments
    pal_execute_vmcall();

    // Xen hypercall ABI using the Intel VMCALL instruction:
    uint64_t index = 0;     // rax
    uint64_t arg1 = 0;      // rdi
    uint64_t arg2 = 0;      // rsi
    uint64_t arg3 = 0;      // rdx
    uint64_t arg4 = 0;      // r10
    uint64_t arg5 = 0;      // r8
    uint64_t arg6 = 0;      // r9
    uint64_t result = pal_execute_vmcall_xen(index, arg1, arg2, arg3, arg4, arg5, arg6);

    // KVM hypercall ABI using the Intel VMCALL instruction:
    index = 0;              // rax
    arg1 = 0;               // rbx
    arg2 = 0;               // rcx
    arg3 = 0;               // rdx
    arg4 = 0;               // rsi
    result = pal_execute_vmcall_kvm(index, arg1, arg2, arg3, arg4);

    // Hyper-V hypercall ABI using the Intel VMCALL instruction:
    index = 0x8001;         // HvExtCallQueryCapabilities
    arg1 = 0;
    result = pal_execute_vmcall_hyperv(index, arg1);
}
