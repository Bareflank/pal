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

#ifndef SHOULDER_AARCH64_GCC_ENCODED_ACCESSORS_H
#define SHOULDER_AARCH64_GCC_ENCODED_ACCESSORS_H

#ifndef SHOULDER_ENCODED_READ
#define SHOULDER_ENCODED_READ(key)                                             \
    uint64_t val;                                                              \
    __asm__ __volatile__(                                                      \
        ".word "#key"\n"                                                       \
        "mov %[v], x0\n"                                                       \
        : [v] "=r"(val)                                                        \
        :                                                                      \
        : "x0"                                                                 \
    );                                                                         \
    return val;
#endif

#ifndef SHOULDER_ENCODED_WRITE
#define SHOULDER_ENCODED_WRITE(key, val)                                       \
    __asm__ __volatile__(                                                      \
        "mov x0, %[v]\n"                                                       \
        ".word "#key"\n"                                                       \
        :                                                                      \
        : [v] "r"(val)                                                         \
        : "x0"                                                                 \
    );
#endif

#ifndef SHOULDER_LDR_IMPL
#define SHOULDER_LDR_IMPL(key) SHOULDER_ENCODED_READ(key)
#endif

#ifndef SHOULDER_MCR_IMPL
#define SHOULDER_MCR_IMPL(key, val) SHOULDER_ENCODED_WRITE(key, val) 
#endif

#ifndef SHOULDER_MCRR_IMPL
#define SHOULDER_MCRR_IMPL(key, val) SHOULDER_ENCODED_WRITE(key, val) 
#endif

#ifndef SHOULDER_MRC_IMPL
#define SHOULDER_MRC_IMPL(key) SHOULDER_ENCODED_READ(key)
#endif

#ifndef SHOULDER_MRRC_IMPL
#define SHOULDER_MRRC_IMPL(key) SHOULDER_ENCODED_READ(key)
#endif

#ifndef SHOULDER_MRS_BANKED_IMPL
#define SHOULDER_MRS_BANKED_IMPL(key) SHOULDER_ENCODED_READ(key)
#endif

#ifndef SHOULDER_MRS_REGISTER_IMPL
#define SHOULDER_MRS_REGISTER_IMPL(key) SHOULDER_ENCODED_READ(key)
#endif

#ifndef SHOULDER_MSR_BANKED_IMPL
#define SHOULDER_MSR_BANKED_IMPL(key, val) SHOULDER_ENCODED_WRITE(key, val) 
#endif

#ifndef SHOULDER_MSR_IMMEDIATE_IMPL
#define SHOULDER_MSR_IMMEDIATE_IMPL(key, val) SHOULDER_ENCODED_WRITE(key, val) 
#endif

#ifndef SHOULDER_MSR_REGISTER_IMPL
#define SHOULDER_MSR_REGISTER_IMPL(key, val) SHOULDER_ENCODED_WRITE(key, val) 
#endif

#ifndef SHOULDER_STR_IMPL
#define SHOULDER_STR_IMPL(key, val) SHOULDER_ENCODED_WRITE(key, val) 
#endif

#ifndef SHOULDER_VMSR_IMPL
#define SHOULDER_VMSR_IMPL(key, val) SHOULDER_ENCODED_WRITE(key, val) 
#endif

#ifndef SHOULDER_VMRS_IMPL
#define SHOULDER_VMRS_IMPL(key) SHOULDER_ENCODED_READ(key)
#endif

#endif
