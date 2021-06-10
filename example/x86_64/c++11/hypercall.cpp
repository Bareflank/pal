#include "pal/instruction/vmcall.h"
#include "pal/instruction/vmcall_xen.h"
#include "pal/instruction/vmcall_kvm.h"

int main()
{
    using namespace pal;

    // Execute the Intel VMCALL instruction with no arguments
    execute_vmcall();

    // Xen hypercall ABI using the Intel VMCALL instruction:
    auto index = 0;     // rax
    auto arg1 = 0;      // rdi
    auto arg2 = 0;      // rsi
    auto arg3 = 0;      // rdx
    auto arg4 = 0;      // r10
    auto arg5 = 0;      // r8
    auto arg6 = 0;      // r9
    auto result = execute_vmcall_xen(index, arg1, arg2, arg3, arg4, arg5, arg6);

    // KVM hypercall ABI using the Intel VMCALL instruction:
    index = 0;              // rax
    arg1 = 0;               // rbx
    arg2 = 0;               // rcx
    arg3 = 0;               // rdx
    arg4 = 0;               // rsi
    result = execute_vmcall_kvm(index, arg1, arg2, arg3, arg4);
}
