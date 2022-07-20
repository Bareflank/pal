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
#define DEVPAL_EXECUTE_SMC 0xFD000002
#define DEVPAL_EXECUTE_HVC 0xFD000003

// ----------------------------------------------------------------------------
struct sys_inputs {
    uint8_t op0;
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
    uint8_t op0;
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

// ----------------------------------------------------------------------------
struct smc_inputs
{
    uint64_t W0;
    uint64_t X1;
    uint64_t X2;
    uint64_t X3;
    uint64_t X4;
    uint64_t X5;
    uint64_t X6;
    uint64_t X7;
    uint64_t X8;
    uint64_t X9;
    uint64_t X10;
    uint64_t X11;
    uint64_t X12;
    uint64_t X13;
    uint64_t X14;
};

struct smc_outputs
{
    uint64_t X0;
    uint64_t X1;
    uint64_t X2;
    uint64_t X3;
    uint64_t X4;
    uint64_t X5;
    uint64_t X6;
    uint64_t X7;
    uint64_t X8;
    uint64_t X9;
    uint64_t X10;
    uint64_t X11;
    uint64_t X12;
    uint64_t X13;
    uint64_t X14;
};

struct smc_operands
{
    struct smc_inputs in;
    struct smc_outputs out;
};

// ----------------------------------------------------------------------------
struct hvc_inputs
{
    uint64_t W0;
    uint64_t X1;
    uint64_t X2;
    uint64_t X3;
    uint64_t X4;
    uint64_t X5;
    uint64_t X6;
    uint64_t X7;
    uint64_t X8;
    uint64_t X9;
    uint64_t X10;
    uint64_t X11;
    uint64_t X12;
    uint64_t X13;
    uint64_t X14;
};

struct hvc_outputs
{
    uint64_t X0;
    uint64_t X1;
    uint64_t X2;
    uint64_t X3;
    uint64_t X4;
    uint64_t X5;
    uint64_t X6;
    uint64_t X7;
    uint64_t X8;
    uint64_t X9;
    uint64_t X10;
    uint64_t X11;
    uint64_t X12;
    uint64_t X13;
    uint64_t X14;
};

struct hvc_operands
{
    struct hvc_inputs in;
    struct hvc_outputs out;
};
#endif
