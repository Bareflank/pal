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

#ifndef ENCODED_ACCESSOR_MACROS_H
#define ENCODED_ACCESSOR_MACROS_H

#ifndef GET_SYSREG
#define GET_SYSREG(encoding, dest)                                             \
    __asm__ __volatile__(                                                      \
        ".word "#encoding"\n"                                                  \
        "mov %0, x0\n"                                                         \
        : "=r"(dest)                                                           \
        : : "x0"                                                               \
    )
#endif

#ifndef SET_SYSREG_BY_VALUE
#define SET_SYSREG_BY_VALUE(encoding, val)                                     \
    __asm__ __volatile__(                                                      \
        "mov x0, %0\n"                                                         \
        ".word "#encoding"\n"                                                  \
        : : "r"(val)                                                           \
        : "x0"                                                                 \
    )
#endif

#ifndef GET_SYSREG_FIELD
#define GET_SYSREG_FIELD(encoding, dest, mask, lsb)                            \
    __asm__ __volatile__(                                                      \
        ".word "#encoding"\n"                                                  \
        "mov %[d], x0\n"                                                       \
        "and %[d], %[d], %[m]\n"                                               \
        "lsr %[d], %[d], #"#lsb"\n"                                            \
        : [d] "+r" (dest)                                                      \
        : [m] "r" (mask)                                                       \
        : "x0"                                                                 \
    )
#endif

#ifndef SET_SYSREG_BITS_BY_VALUE
#define SET_SYSREG_BITS_BY_VALUE(get_encoding, set_encoding,                   \
                                 new_val, old_val, mask, lsb)                  \
    __asm__ __volatile__(                                                      \
        "lsl %[nv], %[nv], #"#lsb"\n"                                          \
        "and %[nv], %[nv], %[m]\n"                                             \
        "mvn %[m], %[m]\n"                                                     \
        ".word "#get_encoding"\n"                                              \
        "mov %[ov], x0\n"                                                      \
        "and %[ov], %[ov], %[m]\n"                                             \
        "orr %[nv], %[nv], %[ov]\n"                                            \
        "mov x0, %[nv]\n"                                                      \
        ".word "#set_encoding"\n"                                              \
        : [nv] "+r" (new_val), [ov] "+r" (old_val), [m] "+r" (mask)            \
        : : "x0"                                                               \
    )
#endif

#ifndef SET_SYSREG_BITS_BY_VALUE_FUNC
#define SET_SYSREG_BITS_BY_VALUE_FUNC(get_encoding, set_encoding,              \
                                      value, bitmask, lsb)                     \
    uint64_t old_val;                                                          \
    uint64_t new_val = value;                                                  \
    uint64_t mask = bitmask;                                                   \
    SET_SYSREG_BITS_BY_VALUE(get_encoding, set_encoding,                       \
                             new_val, old_val, mask, lsb);
#endif

#ifndef IS_SYSREG_BIT_ENABLED
#define IS_SYSREG_BIT_ENABLED(encoding, result, lsb)                           \
    __asm__ __volatile__(                                                      \
        ".word "#encoding"\n"                                                  \
        "mov %[res], x0\n"                                                     \
        "lsr %[res], %[res], #"#lsb"\n"                                        \
        "and %[res], %[res], #1\n"                                             \
        : [res] "+r" (result)                                                  \
        : : "x0"                                                               \
    )
#endif

#ifndef IS_SYSREG_BIT_DISABLED
#define IS_SYSREG_BIT_DISABLED(encoding, result, lsb)                          \
    __asm__ __volatile__(                                                      \
        ".word "#encoding"\n"                                                  \
        "mov %[res], x0\n"                                                     \
        "lsr %[res], %[res], #"#lsb"\n"                                        \
        "mvn %[res], %[res]\n"                                                 \
        "and %[res], %[res], #1\n"                                             \
        : [res] "+r" (result)                                                  \
        : : "x0"                                                               \
    )
#endif

#ifndef SET_SYSREG_BITS_BY_MASK
#define SET_SYSREG_BITS_BY_MASK(get_encoding, set_encoding, val, mask)         \
    __asm__ __volatile__(                                                      \
        ".word "#get_encoding"\n"                                              \
        "mov %[v], x0\n"                                                       \
        "orr %[v], %[v], %[m]\n"                                               \
        "mov x0, %[v]\n"                                                       \
        ".word "#set_encoding"\n"                                              \
        : [v] "+r" (val)                                                       \
        : [m] "r" (mask)                                                       \
        : "x0"                                                                 \
    )
#endif

#ifndef SET_SYSREG_BITS_BY_MASK_FUNC
#define SET_SYSREG_BITS_BY_MASK_FUNC(get_encoding, set_encoding, bitmask)      \
    uint64_t val;                                                              \
    uint64_t mask = bitmask;                                                   \
    SET_SYSREG_BITS_BY_MASK(get_encoding, set_encoding, val, mask);
#endif

#ifndef CLEAR_SYSREG_BITS_BY_MASK
#define CLEAR_SYSREG_BITS_BY_MASK(get_encoding, set_encoding, val, mask)       \
    __asm__ __volatile__(                                                      \
        ".word "#get_encoding"\n"                                              \
        "mov %[v], x0\n"                                                       \
        "mvn %[m], %[m]\n"                                                     \
        "and %[v], %[v], %[m]\n"                                               \
        "mov x0, %[v]\n"                                                       \
        ".word "#set_encoding"\n"                                              \
        : [v] "+r" (val), [m] "+r" (mask)                                      \
        : : "x0"                                                               \
    )
#endif

#ifndef CLEAR_SYSREG_BITS_BY_MASK_FUNC
#define CLEAR_SYSREG_BITS_BY_MASK_FUNC(get_encoding, set_encoding, bitmask)    \
    uint64_t val;                                                              \
    uint64_t mask = bitmask;                                                   \
    CLEAR_SYSREG_BITS_BY_MASK(get_encoding, set_encoding, val, mask);
#endif

#endif
