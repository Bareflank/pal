// ----------------------------------------------------------------------------
// README
// ----------------------------------------------------------------------------
// This file contains aarch64-gcc specific implementations for reading and
// writing system registers via all access mechanisms supported in AArch64
// state. An "implementation" is the body of a function that carries out
// a read/write using a specific access mechanism, used to back generated
// accessor functions from a Shoulder generator

#ifndef SHOULDER_AARCH64_GCC_ACCESSORS_H
#define SHOULDER_AARCH64_GCC_ACCESSORS_H

// Default implementation for reading a value using an instruction encoding from
// aarch64 state. Assumes that the instruction encoding contains x0 as the
// destination register for the read
//
// @arg instruction_encoding a 32-bit binary representation of an instruction
//      that reads data into x0 in aarch64 state
//
// returns the value read through the instruction
#ifndef SHOULDER_AARCH64_ENCODED_READ_IMPL
#define SHOULDER_AARCH64_ENCODED_READ_IMPL(instruction_encoding)               \
    uint64_t val;                                                              \
    __asm__ __volatile__(                                                      \
        ".word "#instruction_encoding"\n"                                      \
        "mov %[v], x0\n"                                                       \
        : [v] "=r"(val)                                                        \
        :                                                                      \
        : "x0"                                                                 \
    );                                                                         \
    return val;
#endif

// Default implementation for writing a value using an instruction encoding from
// aarch64 state. Assumes that the instruction encoding contains x0 as the
// source register for the write
//
// @arg instruction_encoding a 32-bit binary representation of an instruction
//      that writes data from x0 in aarch64 state
// @arg val an integer value to be written
#ifndef SHOULDER_AARCH64_ENCODED_WRITE_IMPL
#define SHOULDER_AARCH64_ENCODED_WRITE_IMPL(instruction_encoding, val)         \
    __asm__ __volatile__(                                                      \
        "mov x0, %[v]\n"                                                       \
        ".word "#instruction_encoding"\n"                                      \
        :                                                                      \
        : [v] "r"(val)                                                         \
        : "x0"                                                                 \
    );
#endif

// Default implementation for reading a value from a system register to a
// general purpose register using the MRS instruction.
//
// @arg sysreg_mnemonic the assmbler mnemonic for the system register to be read
//
// returns the value read from the system register
#ifndef SHOULDER_AARCH64_MRS_REGISTER_IMPL
#define SHOULDER_AARCH64_MRS_REGISTER_IMPL(sysreg_mnemonic)                    \
    uint64_t val;                                                              \
    __asm__ __volatile__(                                                      \
        "mrs %[v], "#sysreg_mnemonic"\n"                                       \
        : [v] "=r"(val)                                                        \
    );                                                                         \
    return val;
#endif

// Default implementation for writing an immediate value to a system register
// using the MSR instruction.
//
// @arg sysreg_mnemonic the assmbler mnemonic for the system register to be
//      written
// @arg val the value to be written
#ifndef SHOULDER_AARCH64_MSR_IMMEDIATE_IMPL
#define SHOULDER_AARCH64_MSR_IMMEDIATE_IMPL(sysreg_mnemonic, val)              \
    __asm__ __volatile__(                                                      \
        "msr "#sysreg_mnemonic", #"val"\n"                                     \
        :                                                                      \
        : [v] "r"(val)                                                         \
    );
#endif

// Default implementation for writing a value to a system register from a
// general purpose register using the MSR instruction.
//
// @arg sysreg_mnemonic the assmbler mnemonic for the system register to be
//      written
// @arg val the value to be written
#ifndef SHOULDER_AARCH64_MSR_REGISTER_IMPL
#define SHOULDER_AARCH64_MSR_REGISTER_IMPL(sysreg_mnemonic, val)               \
    __asm__ __volatile__(                                                      \
        "msr "#sysreg_mnemonic", %[v]\n"                                       \
        :                                                                      \
        : [v] "r"(val)                                                         \
    );
#endif

#endif
