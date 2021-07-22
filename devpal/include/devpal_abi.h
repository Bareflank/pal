#ifndef DEVPAL_ABI_H
#define DEVPAL_ABI_H

#ifdef __kernel__
#include <linux/types.h>
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
        struct in_32_operands in_32_operands;
        struct rdmsr_operands rdmsr_operands;
        struct rdtsc_operands rdtsc_operands;
        struct read_cr0_operands read_cr0_operands;
        struct read_cr2_operands read_cr2_operands;
        struct read_cr3_operands read_cr3_operands;
        struct read_cr4_operands read_cr4_operands;
        struct read_cr8_operands read_cr8_operands;

        // Intel Specific
        struct vmcall_operands vmcall_operands;
    } request_data;
};

typedef struct execute_request cpu_execute_request_t;
typedef struct execute_request cpu_execute_response_t;

#endif
