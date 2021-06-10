#ifndef DEVPAL_ABI_X64_INTEL_H
#define DEVPAL_ABI_X64_INTEL_H

#ifdef __kernel__
#include <linux/types.h>
#else
#include <stdint.h>
#endif

#define DEVPAL_EXECUTE_VMCALL 0xFE000000
#define DEVPAL_EXECUTE_VMCALL_KVM 0xFE000001
#define DEVPAL_EXECUTE_VMCALL_XEN 0xFE000002

// ----------------------------------------------------------------------------
struct vmcall_operands {
    // The vmcall instruction does not logically define inputs or outputs
};
// ----------------------------------------------------------------------------
struct vmcall_hyperv_inputs {
    uint64_t rax;
    uint64_t rbx;
    uint64_t rcx;
    uint64_t rdx;
    uint64_t rsi;
};

struct vmcall_hyperv_outputs {
    uint64_t rax;
};

struct vmcall_hyperv_operands {
    struct vmcall_hyperv_inputs in;
    struct vmcall_hyperv_outputs out;
};
// ----------------------------------------------------------------------------
struct vmcall_kvm_inputs {
    uint64_t rax;
    uint64_t rbx;
    uint64_t rcx;
    uint64_t rdx;
    uint64_t rsi;
};

struct vmcall_kvm_outputs {
    uint64_t rax;
};

struct vmcall_kvm_operands {
    struct vmcall_kvm_inputs in;
    struct vmcall_kvm_outputs out;
};
// ----------------------------------------------------------------------------
struct vmcall_xen_inputs {
    uint64_t rax;
    uint64_t rdi;
    uint64_t rsi;
    uint64_t rdx;
    uint64_t r10;
    uint64_t r8;
    uint64_t r9;
};

struct vmcall_xen_outputs {
    uint64_t rax;
};

struct vmcall_xen_operands {
    struct vmcall_xen_inputs in;
    struct vmcall_xen_outputs out;
};

#endif
