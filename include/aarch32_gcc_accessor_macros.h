// 
// Shoulder
// Copyright (C) 2018 Assured Information Security, Inc.
// 
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
// 
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
// 
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.
// 

// ----------------------------------------------------------------------------
// README
// ----------------------------------------------------------------------------
// This file contains aarch32-gcc specific implementations for reading and
// writing system registers via all access mechanisms supported in AArch32
// state. An "implementation" is the body of a function that carries out
// a read/write using a specific access mechanism, used to back generated
// accessor functions from a Shoulder generator

#ifndef SHOULDER_AARCH32_GCC_ACCESSORS_H
#define SHOULDER_AARCH32_GCC_ACCESSORS_H

// Default implementation for reading a value using an instruction encoding.
// Assumes that the instruction encoding contains r0 as the destination register
// for the read
//
// @arg instruction_encoding a 32-bit binary representation of an instruction
//      that reads data into r0 in aarch32 state
//
// returns the value read through the instruction
#ifndef SHOULDER_AARCH32_ENCODED_READ_IMPL
#define SHOULDER_AARCH32_ENCODED_READ_IMPL(instruction_encoding)               \
    uint32_t val;                                                              \
    __asm__ __volatile__(                                                      \
        ".word "#instruction_encoding"\n"                                      \
        "mov %[v], r0\n"                                                       \
        : [v] "=r"(val)                                                        \
        :                                                                      \
        : "r0"                                                                 \
    );                                                                         \
    return val;
#endif

// Default implementation for writing a value using an instruction encoding.
// Assumes that the instruction encoding contains r0 as the source register
// for the write
//
// @arg instruction_encoding a 32-bit binary representation of an instruction
//      that writes data from r0 in aarch32 state
// @arg val an integer value to be written
#ifndef SHOULDER_AARCH32_ENCODED_WRITE_IMPL
#define SHOULDER_AARCH32_ENCODED_WRITE_IMPL(instruction_encoding, val)         \
    __asm__ __volatile__(                                                      \
        "mov r0, %[v]\n"                                                       \
        ".word "#instruction_encoding"\n"                                      \
        :                                                                      \
        : [v] "r"(val)                                                         \
        : "r0"                                                                 \
    );
#endif

// Default implementation for reading a value using the LDR instruction.
//
// @arg addr the address to read from
#ifndef SHOULDER_AARCH32_LDR_IMPL
#define SHOULDER_AARCH32_LDR_IMPL(addr)                                        \
    uint32_t address = addr;                                                   \
    uint32_t val = 0;                                                          \
    __asm__ __volatile__(                                                      \
        "ldr %[val], %[address]\n"                                             \
        : [val] "=r"(val)                                                      \
        : [address] "r"(address)                                               \
    );                                                                         \
    return val;
#endif

// Default implementation for writing a value to a coprocessor using the MCR
// instruction.
//
// @arg coproc integer value (0-15) that defines the coprocessor number
// @arg opc1 3-bit coprocessor-specific opcode
// @arg crn coprocessor-specific subregister
// @arg crm coprocessor-specific register
// @arg opc2 optional 3-bit coprocessor-specific opcode
// @arg val the value to be written
#ifndef SHOULDER_AARCH32_MCR_IMPL
#define SHOULDER_AARCH32_MCR_IMPL(coproc, opc1, crn, crm, opc2, val)           \
    __asm__ __volatile__(                                                      \
        "mcr p"#coproc", #"#opc1", %[v], c"#crn", c"#crm", #"#opc2"\n"         \
        :                                                                      \
        : [v] "r"(val)                                                         \
    );
#endif

// Default implementation for writing a value to a coprocessor using the MCRR
// instruction.
//
// @arg coproc integer value (0-15) that defines the coprocessor number
// @arg opc1 3-bit coprocessor-specific opcode
// @arg crm coprocessor-specific register
// @arg val the value to be written
#ifndef SHOULDER_AARCH32_MCRR_IMPL
#define SHOULDER_AARCH32_MCRR_IMPL(coproc, opc1, crm, val)                     \
    volatile uint32_t r1 = (uint64_t)val & 0x00000000FFFFFFFF;                 \
    volatile uint32_t r2 = ((uint64_t)val & 0xFFFFFFFF00000000) >> 32;         \
    __asm__ __volatile__(                                                      \
        "mcrr p"#coproc", #"#opc1", %[v1], %[v2], c"#crm"\n"                   \
        :                                                                      \
        : [v1] "r"(r1), [v2] "r"(r2)                                           \
    );
#endif

// Default implementation for reading a value from a coprocessor using the MRC
// instruction.
//
// @arg coproc integer value (0-15) that defines the coprocessor number
// @arg opc1 3-bit coprocessor-specific opcode
// @arg crn coprocessor-specific subregister
// @arg crm coprocessor-specific register
// @arg opc2 optional 3-bit coprocessor-specific opcode
//
// returns the value read from the coprocessor
#ifndef SHOULDER_AARCH32_MRC_IMPL
#define SHOULDER_AARCH32_MRC_IMPL(coproc, opc1, crn, crm, opc2)                \
    uint32_t val;                                                              \
    __asm__ __volatile__(                                                      \
        "mrc p"#coproc", #"#opc1", %[v], c"#crn", c"#crm", #"#opc2"\n"         \
        : [v] "=r"(val)                                                        \
    );                                                                         \
    return val;
#endif

// Default implementation for reading a value from a coprocessor using the MRRC
// instruction.
//
// @arg coproc integer value (0-15) that defines the coprocessor number
// @arg opc1 3-bit coprocessor-specific opcode
// @arg crm coprocessor-specific register
//
// returns the value read from the coprocessor
#ifndef SHOULDER_AARCH32_MRRC_IMPL
#define SHOULDER_AARCH32_MRRC_IMPL(coproc, opc1, crm)                          \
    volatile uint32_t r1 = 0;                                                  \
    volatile uint32_t r2 = 0;                                                  \
    __asm__ __volatile__(                                                      \
        "mrrc p"#coproc", #"#opc1", %[v1], %[v2], c"#crm"\n"                   \
        : [v1] "=r"(r1), [v2] "=r"(r2)                                         \
    );                                                                         \
    return (uint64_t)r1 & ((uint64_t)r2 << 32);
#endif

// Default implementation for reading a value from a banked system register to a
// general purpose register using the MRS instruction.
//
// @arg sysreg_mnemonic the assmbler mnemonic for the system register to be read
//
// returns the value read from the system register
#ifndef SHOULDER_AARCH32_MRS_BANKED_IMPL
#define SHOULDER_AARCH32_MRS_BANKED_IMPL(sysreg_mnemonic)                      \
    uint32_t val;                                                              \
    __asm__ __volatile__(                                                      \
        "mrs %[v], "#sysreg_mnemonic"\n"                                       \
        : [v] "=r"(val)                                                        \
    );                                                                         \
    return val;
#endif

// Default implementation for writing a  value to a banked system register
// from a general purpose register using the MSR instruction.
//
// @arg sysreg_mnemonic the assmbler mnemonic for the system register to be
//      written
// @arg val the value to be written
#ifndef SHOULDER_AARCH32_MSR_BANKED_IMPL
#define SHOULDER_AARCH32_MSR_BANKED_IMPL(sysreg_mnemonic, val)                 \
    __asm__ __volatile__(                                                      \
        "msr "#sysreg_mnemonic", %[v]\n"                                       \
        :                                                                      \
        : [v] "r"(val)                                                         \
    );
#endif

// Default implementation for writing a value using the STR instruction.
//
// @arg addr the address to write to
// @arg val the value to be written
#ifndef SHOULDER_AARCH32_STR_IMPL
#define SHOULDER_AARCH32_STR_IMPL(addr, val)                                   \
    uint32_t address = addr;                                                   \
    uint32_t result = 0;                                                       \
    __asm__ __volatile__(                                                      \
        "str %[res], %[address]\n"                                             \
        :                                                                      \
        : [address] "r"(address), [res] "r"(result)                            \
    );
#endif

// Default implementation for writing a value to a NEON/VFP system register
// from a general purpose register using the VMSR instruction.
//
// @arg extsysreg_mnemonic the assmbler mnemonic for the NEON/VFP system
//      register to be written
// @arg val the value to be written
#ifndef SHOULDER_AARCH32_VMSR_IMPL
#define SHOULDER_AARCH32_VMSR_IMPL(extsysreg_mnemonic, val)                    \
    __asm__ __volatile__(                                                      \
        "vmsr "#extsysreg_mnemonic", %[v]\n"                                   \
        :                                                                      \
        : [v] "r"(val)                                                         \
    );
#endif

// Default implementation for reading a value from a NEON/VFP system register
// to a general purpose register using the VMRS instruction.
//
// @arg extsysreg_mnemonic the assmbler mnemonic for the NEON/VFP system
//      register to be read
//
// returns the value read from the system register
#ifndef SHOULDER_AARCH32_VMRS_IMPL
#define SHOULDER_AARCH32_VMRS_IMPL(extsysreg_mnemonic)                         \
    uint32_t val;                                                              \
    __asm__ __volatile__(                                                      \
        "vmrs %[v], "#extsysreg_mnemonic"\n"                                   \
        : [v] "=r"(val)                                                        \
    );                                                                         \
    return val;
#endif

#endif
