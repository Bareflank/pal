#ifndef DEVPAL_ABI_H
#define DEVPAL_ABI_H

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

#include "devpal_abi_armv8a_aarch64.h"
#include "devpal_abi_generic.h"
#include "devpal_abi_x64.h"
#include "devpal_abi_x64_intel.h"

struct execute_request {
    uint64_t request_code;
    union {
        // Generic
        struct read_mem8_operands read_mem8_operands;
        struct read_mem16_operands read_mem16_operands;
        struct read_mem32_operands read_mem32_operands;
        struct read_mem64_operands read_mem64_operands;
        struct write_mem8_operands write_mem8_operands;
        struct write_mem16_operands write_mem16_operands;
        struct write_mem32_operands write_mem32_operands;
        struct write_mem64_operands write_mem64_operands;

        // Generic x86_64
        struct cpuid_operands cpuid_operands;
        struct in_8_operands in_8_operands;
        struct in_16_operands in_16_operands;
        struct in_32_operands in_32_operands;
        struct out_8_operands out_8_operands;
        struct out_16_operands out_16_operands;
        struct out_32_operands out_32_operands;
        struct rdmsr_operands rdmsr_operands;
        struct rdtsc_operands rdtsc_operands;
        struct read_cr0_operands read_cr0_operands;
        struct read_cr2_operands read_cr2_operands;
        struct read_cr3_operands read_cr3_operands;
        struct read_cr4_operands read_cr4_operands;
        struct read_cr8_operands read_cr8_operands;

        // Intel Specific
        struct vmcall_kvm_operands vmcall_kvm_operands;
        struct vmcall_xen_operands vmcall_xen_operands;
    } request_data;
};

typedef struct execute_request cpu_execute_request_t;
typedef struct execute_request cpu_execute_response_t;

#endif
