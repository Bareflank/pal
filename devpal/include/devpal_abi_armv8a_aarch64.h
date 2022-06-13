#ifndef DEVPAL_ABI_ARMV8_AARCH64_H
#define DEVPAL_ABI_ARMV8_AARCH64_H

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

#define DEVPAL_EXECUTE_SYS 0xFD000000
#define DEVPAL_EXECUTE_SYSL 0xFD000001

// ----------------------------------------------------------------------------
struct sys_inputs {
    uint8_t op1;
    uint8_t crn;
    uint8_t crm;
    uint8_t op2;
    uint64_t value;
};

struct sys_operands {
    struct sys_inputs in;
};
// ----------------------------------------------------------------------------
struct sysl_inputs {
    uint8_t op1;
    uint8_t crn;
    uint8_t crm;
    uint8_t op2;
};

struct sysl_outputs {
    uint64_t value;
};

struct sysl_operands {
    struct sysl_inputs in;
    struct sysl_outputs out;
};

#endif
