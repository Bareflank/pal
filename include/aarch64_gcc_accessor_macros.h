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
// This file contains aarch64-gcc specific implementations for reading and
// writing system registers via all access mechanisms supported in the AArch64
// architecture. An "implementation" is the body of a function that carries out
// a read/write using a specific access mechanism, used to back generated
// accessor functions from a Shoulder generator

#ifndef SHOULDER_AARCH64_GCC_ACCESSORS_H
#define SHOULDER_AARCH64_GCC_ACCESSORS_H

// Default implementation for reading a value using an instruction encoding.
// Assumes that the instruction encoding contains r0 as the destination register
// for the read
//
// @arg instruction_encoding a 32-bit binary representation of an instruction
//      that reads data into r0
//
// returns the value read through the instruction
#ifndef SHOULDER_ENCODED_READ_IMPL
#define SHOULDER_ENCODED_READ_IMPL(instruction_encoding)                       \
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

// Default implementation for writing a value using an instruction encoding.
// Assumes that the instruction encoding contains r0 as the source register
// for the write
//
// @arg instruction_encoding a 32-bit binary representation of an instruction
//      that writes data from r0
// @arg val an integer value to be written
#ifndef SHOULDER_ENCODED_WRITE_IMPL
#define SHOULDER_ENCODED_WRITE_IMPL(instruction_encoding, val)                 \
    __asm__ __volatile__(                                                      \
        "mov x0, %[v]\n"                                                       \
        ".word "#instruction_encoding"\n"                                      \
        :                                                                      \
        : [v] "r"(val)                                                         \
        : "x0"                                                                 \
    );
#endif

// Default implementation for reading a value using the LDR instruction.
//
// @arg addr the address to read from
#ifndef SHOULDER_LDR_IMPL
#define SHOULDER_LDR_IMPL(addr)                                                \
    "TODO: LDR using assembler mnemonics"
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
#ifndef SHOULDER_MCR_IMPL
#define SHOULDER_MCR_IMPL(coproc, opc1, crn, crm, opc2, val)                   \
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
#ifndef SHOULDER_MCRR_IMPL
#define SHOULDER_MCRR_IMPL(coproc, opc1, crm, val)                             \
    "TODO: MCRR using assembler mnemonics"
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
#ifndef SHOULDER_MRC_IMPL
#define SHOULDER_MRC_IMPL(coproc, opc1, crn, crm, opc2)                        \
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
#ifndef SHOULDER_MRRC_IMPL
#define SHOULDER_MRRC_IMPL(coproc, opc1, crm)                                  \
    "TODO: MRRC using assembler mnemonics"
#endif

// Default implementation for reading a value from a banked system register to a
// general purpose register using the MRS instruction.
//
// @arg sysreg_mnemonic the assmbler mnemonic for the system register to be read
//
// returns the value read from the system register
#ifndef SHOULDER_MRS_BANKED_IMPL
#define SHOULDER_MRS_BANKED_IMPL(sysreg_mnemonic)                              \
    "TODO: MRS_BANKED using assembler mnemonics"
#endif

// Default implementation for reading a value from a system register to a
// general purpose register using the MRS instruction.
//
// @arg sysreg_mnemonic the assmbler mnemonic for the system register to be read
//
// returns the value read from the system register
#ifndef SHOULDER_MRS_REGISTER_IMPL
#define SHOULDER_MRS_REGISTER_IMPL(sysreg_mnemonic)                            \
    uint64_t val;                                                              \
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
#ifndef SHOULDER_MSR_BANKED_IMPL
#define SHOULDER_MSR_BANKED_IMPL(sysreg_mnemonic, val)                         \
    "TODO: MSR_BANKED using assembler mnemonics"
#endif

// Default implementation for writing an immediate value to a system register
// using the MSR instruction.
//
// @arg sysreg_mnemonic the assmbler mnemonic for the system register to be
//      written
// @arg val the value to be written
#ifndef SHOULDER_MSR_IMMEDIATE_IMPL
#define SHOULDER_MSR_IMMEDIATE_IMPL(sysreg_mnemonic, val)                      \
    "TODO: MSR_IMMEDIATE using assembler mnemonics"
#endif

// Default implementation for writing a value to a system register from a
// general purpose register using the MSR instruction.
//
// @arg sysreg_mnemonic the assmbler mnemonic for the system register to be
//      written
// @arg val the value to be written
#ifndef SHOULDER_MSR_REGISTER_IMPL
#define SHOULDER_MSR_REGISTER_IMPL(sysreg_mnemonic, val)                       \
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
#ifndef SHOULDER_STR_IMPL
#define SHOULDER_STR_IMPL(addr, val)                                           \
    "TODO: STR using assembler mnemonics"
#endif

// Default implementation for writing a value to a NEON/VFP system register
// from a general purpose register using the VMSR instruction.
//
// @arg extsysreg_mnemonic the assmbler mnemonic for the NEON/VFP system
//      register to be written
// @arg val the value to be written
#ifndef SHOULDER_VMSR_IMPL
#define SHOULDER_VMSR_IMPL(extsysreg_mnemonic, val)                            \
    "TODO: VMSR using assembler mnemonics"
#endif

// Default implementation for reading a value from a NEON/VFP system register
// to a general purpose register using the VMRS instruction.
//
// @arg extsysreg_mnemonic the assmbler mnemonic for the NEON/VFP system
//      register to be read
//
// returns the value read from the system register
#ifndef SHOULDER_VMRS_IMPL
#define SHOULDER_VMRS_IMPL(extsysreg_mnemonic)                                 \
    "TODO: VMRS using assembler mnemonics"
#endif

#endif
