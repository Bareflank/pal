#ifndef DEVPAL_ABI_ARMV8_AARCH64_H
#define DEVPAL_ABI_ARMV8_AARCH64_H

#ifdef __kernel__
#include <linux/types.h>
#else
#include <stdint.h>
#endif

#define DEVPAL_EXECUTE_SYS 0xFD000000
#define DEVPAL_EXECUTE_SYSL 0xFD000001

// ----------------------------------------------------------------------------
struct sys_inputs {
    uint64_t op1;
    uint64_t crn;
    uint64_t crm;
    uint64_t op2;
};

struct sys_operands {
    struct sys_inputs in;
};
// ----------------------------------------------------------------------------
struct sysl_inputs {
    uint64_t op1;
    uint64_t crn;
    uint64_t crm;
    uint64_t op2;
};

struct sysl_outputs {
    uint64_t value;
};

struct sysl_operands {
    struct sysl_inputs in;
    struct sysl_outputs out;
};

#endif
