#ifndef DEVPAL_ABI_X64_H
#define DEVPAL_ABI_X64_H

#ifdef __kernel__
#include <linux/types.h>
#else
#include <stdint.h>
#endif

#define DEVPAL_EXECUTE_CPUID 0xFF000000
#define DEVPAL_EXECUTE_IN_32 0xFF000001
#define DEVPAL_EXECUTE_RDMSR 0xFF000002
#define DEVPAL_EXECUTE_RDTSC 0xFF000003
#define DEVPAL_EXECUTE_READ_CR0 0xFF000004
#define DEVPAL_EXECUTE_READ_CR2 0xFF000005
#define DEVPAL_EXECUTE_READ_CR3 0xFF000006
#define DEVPAL_EXECUTE_READ_CR4 0xFF000007
#define DEVPAL_EXECUTE_READ_CR8 0xFF000008
#define DEVPAL_EXECUTE_READ_CS 0xFF000009
#define DEVPAL_EXECUTE_READ_DR7 0xFF00000A
#define DEVPAL_EXECUTE_READ_DS 0xFF00000B
#define DEVPAL_EXECUTE_READ_ES 0xFF00000C
#define DEVPAL_EXECUTE_READ_FS 0xFF00000D
#define DEVPAL_EXECUTE_READ_GS 0xFF00000E
#define DEVPAL_EXECUTE_READ_LDTR 0xFF00000F
#define DEVPAL_EXECUTE_READ_SS 0xFF000010
#define DEVPAL_EXECUTE_READ_TR 0xFF000011
#define DEVPAL_EXECUTE_XGETBV 0xFF000012
#define DEVPAL_EXECUTE_OUT_32 0xFF000013
#define DEVPAL_EXECUTE_WRMSR 0xFF000014

// ----------------------------------------------------------------------------
struct cpuid_inputs {
    uint32_t leaf;
    uint32_t subleaf;
};

struct cpuid_outputs {
    uint32_t eax;
    uint32_t ebx;
    uint32_t ecx;
    uint32_t edx;
};

struct cpuid_operands {
    struct cpuid_inputs in;
    struct cpuid_outputs out;
};
// ----------------------------------------------------------------------------
struct in_32_inputs {
    uint16_t address;
};

struct in_32_outputs {
    uint32_t value;
};

struct in_32_operands {
    struct in_32_inputs in;
    struct in_32_outputs out;
};
// ----------------------------------------------------------------------------
struct out_32_inputs {
    uint16_t address;
    uint32_t value;
};

struct out_32_operands {
    struct out_32_inputs in;
};
// ----------------------------------------------------------------------------
struct rdmsr_inputs {
    uint32_t address;
};

struct rdmsr_outputs {
    uint64_t value;
};

struct rdmsr_operands {
    struct rdmsr_inputs in;
    struct rdmsr_outputs out;
};
// ----------------------------------------------------------------------------
struct rdtsc_outputs {
    uint64_t value;
};

struct rdtsc_operands {
    struct rdtsc_outputs out;
};
// ----------------------------------------------------------------------------
struct read_cr0_outputs {
    uint64_t value;
};

struct read_cr0_operands {
    struct read_cr0_outputs out;
};
// ----------------------------------------------------------------------------
struct read_cr2_outputs {
    uint64_t value;
};

struct read_cr2_operands {
    struct read_cr2_outputs out;
};
// ----------------------------------------------------------------------------
struct read_cr3_outputs {
    uint64_t value;
};

struct read_cr3_operands {
    struct read_cr3_outputs out;
};
// ----------------------------------------------------------------------------
struct read_cr4_outputs {
    uint64_t value;
};

struct read_cr4_operands {
    struct read_cr4_outputs out;
};
// ----------------------------------------------------------------------------
struct read_cr8_outputs {
    uint64_t value;
};

struct read_cr8_operands {
    struct read_cr8_outputs out;
};
// ----------------------------------------------------------------------------
struct wrmsr_inputs {
    uint32_t address;
    uint64_t value;
};

struct wrmsr_operands {
    struct wrmsr_inputs in;
};
// ----------------------------------------------------------------------------

#endif
