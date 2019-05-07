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

#ifndef SHOULDER_AARCH64_GCC_MNEMONIC_ACCESSORS_H
#define SHOULDER_AARCH64_GCC_MNEMONIC_ACCESSORS_H

#ifndef SHOULDER_LDR_IMPL
#define SHOULDER_LDR_IMPL(key)                                                 \
    "TODO: LDR using assembler mnemonics"
#endif

#ifndef SHOULDER_MCR_IMPL
#define SHOULDER_MCR_IMPL(key, val)                                            \
    "TODO: MCR using assembler mnemonics"
#endif

#ifndef SHOULDER_MCRR_IMPL
#define SHOULDER_MCRR_IMPL(key, val)                                           \
    "TODO: MCRR using assembler mnemonics"
#endif

#ifndef SHOULDER_MRC_IMPL
#define SHOULDER_MRC_IMPL(key)                                                 \
    "TODO: MRC using assembler mnemonics"
#endif

#ifndef SHOULDER_MRRC_IMPL
#define SHOULDER_MRRC_IMPL(key)                                                \
    "TODO: MRRC using assembler mnemonics"
#endif

#ifndef SHOULDER_MRS_BANKED_IMPL
#define SHOULDER_MRS_BANKED_IMPL(key)                                          \
    "TODO: MRS_BANKED using assembler mnemonics"
#endif

#ifndef SHOULDER_MRS_REGISTER_IMPL
#define SHOULDER_MRS_REGISTER_IMPL(key)                                        \
    uint64_t val;                                                              \
    __asm__ __volatile__(                                                      \
        "mrs %0, "#key"\n"                                                     \
        : "=r"(val)                                                            \
    );                                                                         \
    return val;
#endif

#ifndef SHOULDER_MSR_BANKED_IMPL
#define SHOULDER_MSR_BANKED_IMPL(key, val)                                     \
    "TODO: MSR_BANKED using assembler mnemonics"
#endif

#ifndef SHOULDER_MSR_IMMEDIATE_IMPL
#define SHOULDER_MSR_IMMEDIATE_IMPL(key, val)                                  \
    "TODO: MSR_IMMEDIATE using assembler mnemonics"
#endif

#ifndef SHOULDER_MSR_REGISTER_IMPL
#define SHOULDER_MSR_REGISTER_IMPL(key, val)                                   \
    __asm__ __volatile__(                                                      \
        "msr "#key", %[v]\n"                                                   \
        :                                                                      \
        : [v] "r"(val)                                                         \
    );
#endif

#ifndef SHOULDER_STR_IMPL
#define SHOULDER_STR_IMPL(key, val)                                            \
    "TODO: STR using assembler mnemonics"
#endif

#ifndef SHOULDER_VMSR_IMPL
#define SHOULDER_VMSR_IMPL(key, val)                                           \
    "TODO: VMSR using assembler mnemonics"
#endif

#ifndef SHOULDER_VMRS_IMPL
#define SHOULDER_VMRS_IMPL(key)                                                \
    "TODO: VMRS using assembler mnemonics"
#endif

#endif
