#ifndef DEVPAL_ABI_X64_H
#define DEVPAL_ABI_X64_H

#ifdef __kernel__
#include <linux/types.h>
#elif _KERNEL_MODE
#include <ntddk.h>
typedef UINT8 uint8_t;
typedef UINT16 uint16_t;
typedef UINT32 uint32_t;
typedef UINT64 uint64_t;
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
#define DEVPAL_EXECUTE_OUT_32 0xFF000013
#define DEVPAL_EXECUTE_WRMSR 0xFF000014
#define DEVPAL_EXECUTE_IN_8 0xFF000015
#define DEVPAL_EXECUTE_IN_16 0xFF000016
#define DEVPAL_EXECUTE_OUT_8 0xFF000017
#define DEVPAL_EXECUTE_OUT_16 0xFF000018
#define DEVPAL_EXECUTE_WRITE_CR0 0xFF00019
#define DEVPAL_EXECUTE_WRITE_CR2 0xFF000020
#define DEVPAL_EXECUTE_WRITE_CR3 0xFF000021
#define DEVPAL_EXECUTE_WRITE_CR4 0xFF000022
#define DEVPAL_EXECUTE_WRITE_CR8 0xFF000023
#define DEVPAL_EXECUTE_XGETBV 0xFF000024
#define DEVPAL_EXECUTE_XSETBV 0xFF000025

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
struct in_8_inputs {
    uint16_t address;
};

struct in_8_outputs {
    uint8_t value;
};

struct in_8_operands {
    struct in_8_inputs in;
    struct in_8_outputs out;
};
// ----------------------------------------------------------------------------
struct in_16_inputs {
    uint16_t address;
};

struct in_16_outputs {
    uint16_t value;
};

struct in_16_operands {
    struct in_16_inputs in;
    struct in_16_outputs out;
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
struct out_8_inputs {
    uint16_t address;
    uint8_t value;
};

struct out_8_operands {
    struct out_8_inputs in;
};
// ----------------------------------------------------------------------------
struct out_16_inputs {
    uint16_t address;
    uint16_t value;
};

struct out_16_operands {
    struct out_16_inputs in;
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
struct write_cr0_inputs {
    uint64_t value;
};

struct write_cr0_operands {
    struct write_cr0_inputs in;
};
// ----------------------------------------------------------------------------
struct write_cr2_inputs {
    uint64_t value;
};

struct write_cr2_operands {
    struct write_cr2_inputs in;
};
// ----------------------------------------------------------------------------
struct write_cr3_inputs {
    uint64_t value;
};

struct write_cr3_operands {
    struct write_cr3_inputs in;
};
// ----------------------------------------------------------------------------
struct write_cr4_inputs {
    uint64_t value;
};

struct write_cr4_operands {
    struct write_cr4_inputs in;
};
// ----------------------------------------------------------------------------
struct write_cr8_inputs {
    uint64_t value;
};

struct write_cr8_operands {
    struct write_cr8_inputs in;
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
struct xgetbv_inputs {
    uint32_t xcr;
};

struct xgetbv_outputs {
    uint64_t value;
};

struct xgetbv_operands {
    struct xgetbv_inputs in;
    struct xgetbv_outputs out;
};
// ----------------------------------------------------------------------------
struct xsetbv_inputs {
    uint32_t xcr;
    uint64_t value;
};

struct xsetbv_operands {
    struct xsetbv_inputs in;
};
// ----------------------------------------------------------------------------

#endif
