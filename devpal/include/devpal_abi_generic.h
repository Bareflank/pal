#ifndef DEVPAL_ABI_GENERIC_H
#define DEVPAL_ABI_GENERIC_H

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

#define DEVPAL_EXECUTE_READ_MEM8 0xFFFF0000
#define DEVPAL_EXECUTE_READ_MEM16 0xFFFF0001
#define DEVPAL_EXECUTE_READ_MEM32 0xFFFF0002
#define DEVPAL_EXECUTE_READ_MEM64 0xFFFF0003
#define DEVPAL_EXECUTE_WRITE_MEM8 0xFFFF0004
#define DEVPAL_EXECUTE_WRITE_MEM16 0xFFFF0005
#define DEVPAL_EXECUTE_WRITE_MEM32 0xFFFF0006
#define DEVPAL_EXECUTE_WRITE_MEM64 0xFFFF0007

// ----------------------------------------------------------------------------
struct read_mem8_inputs {
    uintptr_t address;
};

struct read_mem8_outputs {
    uint8_t value;
};

struct read_mem8_operands {
    struct read_mem8_inputs in;
    struct read_mem8_outputs out;
};
// ----------------------------------------------------------------------------
struct read_mem16_inputs {
    uintptr_t address;
};

struct read_mem16_outputs {
    uint16_t value;
};

struct read_mem16_operands {
    struct read_mem16_inputs in;
    struct read_mem16_outputs out;
};
// ----------------------------------------------------------------------------
struct read_mem32_inputs {
    uintptr_t address;
};

struct read_mem32_outputs {
    uint32_t value;
};

struct read_mem32_operands {
    struct read_mem32_inputs in;
    struct read_mem32_outputs out;
};
// ----------------------------------------------------------------------------
struct read_mem64_inputs {
    uintptr_t address;
};

struct read_mem64_outputs {
    uint64_t value;
};

struct read_mem64_operands {
    struct read_mem64_inputs in;
    struct read_mem64_outputs out;
};
// ----------------------------------------------------------------------------
struct write_mem8_inputs {
    uintptr_t address;
    uint8_t value;
};

struct write_mem8_operands {
    struct write_mem8_inputs in;
};
// ----------------------------------------------------------------------------
struct write_mem16_inputs {
    uintptr_t address;
    uint16_t value;
};

struct write_mem16_operands {
    struct write_mem16_inputs in;
};
// ----------------------------------------------------------------------------
struct write_mem32_inputs {
    uintptr_t address;
    uint32_t value;
};

struct write_mem32_operands {
    struct write_mem32_inputs in;
};
// ----------------------------------------------------------------------------
struct write_mem64_inputs {
    uintptr_t address;
    uint64_t value;
};

struct write_mem64_operands {
    struct write_mem64_inputs in;
};
// ----------------------------------------------------------------------------

#endif
