#ifndef DEVPAL_ABI_H
#define DEVPAL_ABI_H

#ifdef __kernel__
#include <linux/types.h>
#else
#include <stdint.h>
#endif

#include "devpal_abi_armv8a_aarch64.h"
#include "devpal_abi_x64.h"
#include "devpal_abi_x64_intel.h"

struct execute_request {
    uint64_t request_code;
    union {
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
