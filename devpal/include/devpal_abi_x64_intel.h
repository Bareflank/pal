#ifndef DEVPAL_ABI_X64_INTEL_H
#define DEVPAL_ABI_X64_INTEL_H

#ifdef __kernel__
#include <linux/types.h>
#else
#include <stdint.h>
#endif

#define DEVPAL_EXECUTE_VMCALL 0xFE000000

// ----------------------------------------------------------------------------
struct vmcall_inputs {
    uint64_t rax;
    uint64_t rbx;
    uint64_t rcx;
    uint64_t rdx;
    uint64_t rdi;
    uint64_t rsi;
    uint64_t r8;
    uint64_t r9;
    uint64_t r10;
    uint64_t r11;
};

struct vmcall_outputs {
    uint64_t rax;
    uint64_t rbx;
    uint64_t rcx;
    uint64_t rdx;
    uint64_t rdi;
    uint64_t rsi;
    uint64_t r8;
    uint64_t r9;
    uint64_t r10;
    uint64_t r11;
};

struct vmcall_operands {
    struct vmcall_inputs in;
    struct vmcall_outputs out;
};

#endif
