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

#ifndef INTRINSICS_AARCH64_REGS_H
#define INTRINSICS_AARCH64_REGS_H

// -----------------------------------------------------------------------------
// General Purpose Registers
// -----------------------------------------------------------------------------

#ifndef GET_REG32
#define GET_REG32(reg, result)                                                 \
    __asm__ __volatile__(                                                      \
        "mov %w[res], "#reg"\n"                                                \
        : [res] "=r" (result)                                                  \
    )
#endif

#ifndef GET_REG32_FUNC
#define GET_REG32_FUNC(reg)                                                    \
    uint32_t val;                                                              \
    GET_REG32(reg, val);                                                       \
    return val;
#endif

#ifndef GET_REG64
#define GET_REG64(reg, result)                                                 \
    __asm__ __volatile__(                                                      \
        "mov %[res], "#reg"\n"                                                 \
        : [res] "=r" (result)                                                  \
    )
#endif

#ifndef GET_REG64_FUNC
#define GET_REG64_FUNC(reg)                                                    \
    uint64_t val;                                                              \
    GET_REG64(reg, val);                                                       \
    return val;
#endif

#ifndef SET_REG32
#define SET_REG32(reg, val)                                                    \
    __asm__ __volatile__(                                                      \
        "mov "#reg", %w0\n"                                                    \
        : : "r"(val) : #reg                                                    \
    )
#endif

#ifndef SET_REG32_FUNC
#define SET_REG32_FUNC(reg, val)                                               \
    SET_REG32(reg, val);
#endif

#ifndef SET_REG64
#define SET_REG64(reg, val)                                                    \
    __asm__ __volatile__(                                                      \
        "mov "#reg", %0\n"                                                     \
        : : "r"(val) : #reg                                                    \
    )
#endif

#ifndef SET_REG64_FUNC
#define SET_REG64_FUNC(reg, val)                                               \
    SET_REG64(reg, val);
#endif

// -----------------------------------------------------------------------------
// Immediate Values
// -----------------------------------------------------------------------------

#ifndef GET_BITFIELD
#define GET_BITFIELD(val, mask, lsb)                                           \
    __asm__ __volatile__(                                                      \
        "and %[v], %[v], %[m]\n"                                               \
        "lsr %[v], %[v], #"#lsb"\n"                                            \
        : [v] "+r" (val)                                                       \
        : [m] "r" (mask)                                                       \
    )
#endif

#ifndef GET_BITFIELD_FUNC
#define GET_BITFIELD_FUNC(reg_val, bitmask, lsb)                               \
    uint64_t val = reg_val;                                                    \
    uint64_t mask = bitmask;                                                   \
    GET_BITFIELD(val, mask, lsb);                                              \
    return val;
#endif

#ifndef SET_BITS_BY_VALUE
#define SET_BITS_BY_VALUE(reg_val, field_val, mask, lsb)                       \
    __asm__ __volatile__(                                                      \
        "lsl %[fv], %[fv], #"#lsb"\n"                                          \
        "and %[fv], %[fv], %[m]\n"                                             \
        "mvn %[m], %[m]\n"                                                     \
        "and %[rv], %[rv], %[m]\n"                                             \
        "orr %[rv], %[rv], %[fv]\n"                                            \
        : [rv] "+r" (reg_val), [fv] "+r" (field_val), [m] "+r" (mask)          \
    )
#endif

#ifndef SET_BITS_BY_VALUE_FUNC
#define SET_BITS_BY_VALUE_FUNC(reg_val, field_val, bitmask, lsb)               \
    uint64_t rv = reg_val;                                                     \
    uint64_t fv = field_val;                                                   \
    uint64_t mask = bitmask;                                                   \
    SET_BITS_BY_VALUE(rv, fv, mask, lsb);                                      \
    return rv;
#endif

#ifndef SET_BITS_BY_MASK
#define SET_BITS_BY_MASK(value, mask)                                          \
    __asm__ __volatile__(                                                      \
        "orr %[v], %[v], %[m]\n"                                               \
        : [v] "+r" (value) : [m] "r" (mask)                                    \
    )
#endif

#ifndef SET_BITS_BY_MASK_FUNC
#define SET_BITS_BY_MASK_FUNC(value, bitmask)                                  \
    uint64_t val = value;                                                      \
    uint64_t mask = bitmask;                                                   \
    SET_BITS_BY_MASK(val, mask);                                               \
    return val;
#endif

#ifndef CLEAR_BITS_BY_MASK
#define CLEAR_BITS_BY_MASK(value, mask)                                        \
    __asm__ __volatile__(                                                      \
        "mvn %[m], %[m]\n"                                                     \
        "and %[v], %[v], %[m]\n"                                               \
        : [v] "+r" (value), [m] "+r" (mask)                                    \
    )
#endif

#ifndef CLEAR_BITS_BY_MASK_FUNC
#define CLEAR_BITS_BY_MASK_FUNC(value, bitmask)                                \
    uint64_t val = value;                                                      \
    uint64_t mask = bitmask;                                                   \
    CLEAR_BITS_BY_MASK(val, mask);                                             \
    return val;
#endif

#ifndef IS_BIT_ENABLED
#define IS_BIT_ENABLED(var, result, bit_position)                              \
    __asm__ __volatile__(                                                      \
        "mov %[res], %["#var"]\n"                                              \
        "lsr %[res], %[res], #"#bit_position"\n"                               \
        "and %[res], %[res], #1\n"                                             \
        : [res] "=r" (result) : [var] "r" (var)                                \
    )
#endif

#ifndef IS_BIT_ENABLED_FUNC
#define IS_BIT_ENABLED_FUNC(var, bit_position)                                 \
    uint64_t result;                                                           \
    IS_BIT_ENABLED(var, result, bit_position);                                 \
    return result;
#endif

#ifndef IS_BIT_DISABLED
#define IS_BIT_DISABLED(var, result, bit_position)                             \
    __asm__ __volatile__(                                                      \
        "mov %[res], %["#var"]\n"                                              \
        "lsr %[res], %[res], #"#bit_position"\n"                               \
        "mvn %[res], %[res]\n"                                                 \
        "and %[res], %[res], #1\n"                                             \
        : [res] "=r" (result) : [var] "r" (var)                                \
    )
#endif

#ifndef IS_BIT_DISABLED_FUNC
#define IS_BIT_DISABLED_FUNC(var, bit_position)                                \
    uint64_t result;                                                           \
    IS_BIT_DISABLED(var, result, bit_position);                                \
    return result;
#endif

// -----------------------------------------------------------------------------
// System Registers
// -----------------------------------------------------------------------------

#ifndef GET_SYSREG
#define GET_SYSREG(sysreg, dest)                                               \
    __asm__ __volatile__(                                                      \
        "mrs %0, "#sysreg"\n"                                                  \
        : "=r"(dest)                                                           \
    )
#endif

#ifndef GET_SYSREG_FUNC
#define GET_SYSREG_FUNC(reg)                                                   \
    uint64_t val;                                                              \
    GET_SYSREG(reg, val);                                                      \
    return val;
#endif

#ifndef GET_SYSREG_FIELD
#define GET_SYSREG_FIELD(sysreg, dest, mask, lsb)                              \
    __asm__ __volatile__(                                                      \
        "mrs %[d], "#sysreg"\n"                                                \
        "and %[d], %[d], %[m]\n"                                               \
        "lsr %[d], %[d], #"#lsb"\n"                                            \
        : [d] "+r" (dest)                                                      \
        : [m] "r" (mask)                                                       \
    )
#endif

#ifndef GET_SYSREG_FIELD_FUNC
#define GET_SYSREG_FIELD_FUNC(sysreg, bitmask, lsb)                            \
    uint64_t val;                                                              \
    GET_SYSREG_FIELD(sysreg, val, bitmask, lsb);                               \
    return val;
#endif

#ifndef SET_SYSREG_BY_VALUE
#define SET_SYSREG_BY_VALUE(sysreg, val)                                       \
    __asm__ __volatile__(                                                      \
        "msr "#sysreg", %[v]\n"                                                \
        : : [v] "r"(val)                                                       \
    )
#endif

#ifndef SET_SYSREG_BY_VALUE_FUNC
#define SET_SYSREG_BY_VALUE_FUNC(sysreg, val)                                  \
    SET_SYSREG_BY_VALUE(sysreg, val);
#endif

#ifndef SET_SYSREG_BITS_BY_VALUE
#define SET_SYSREG_BITS_BY_VALUE(sysreg, new_val, old_val, mask, lsb)          \
    __asm__ __volatile__(                                                      \
        "lsl %[nv], %[nv], #"#lsb"\n"                                          \
        "and %[nv], %[nv], %[m]\n"                                             \
        "mvn %[m], %[m]\n"                                                     \
        "mrs %[ov], "#sysreg"\n"                                               \
        "and %[ov], %[ov], %[m]\n"                                             \
        "orr %[nv], %[nv], %[ov]\n"                                            \
        "msr "#sysreg", %[nv]\n"                                               \
        : [nv] "+r" (new_val), [ov] "+r" (old_val), [m] "+r" (mask)            \
    )
#endif

#ifndef SET_SYSREG_BITS_BY_VALUE_FUNC
#define SET_SYSREG_BITS_BY_VALUE_FUNC(sysreg, value, bitmask, lsb)             \
    uint64_t old_val;                                                          \
    uint64_t new_val = value;                                                  \
    uint64_t mask = bitmask;                                                   \
    SET_SYSREG_BITS_BY_VALUE(sysreg, new_val, old_val, mask, lsb);
#endif

#ifndef SET_SYSREG_BITS_BY_MASK
#define SET_SYSREG_BITS_BY_MASK(sysreg, val, mask)                             \
    __asm__ __volatile__(                                                      \
        "mrs %[v], "#sysreg"\n"                                                \
        "orr %[v], %[v], %[m]\n"                                               \
        "msr "#sysreg", %[v]\n"                                                \
        : [v] "+r" (val)                                                       \
        : [m] "r" (mask)                                                       \
    )
#endif

#ifndef SET_SYSREG_BITS_BY_MASK_FUNC
#define SET_SYSREG_BITS_BY_MASK_FUNC(sysreg, bitmask)                          \
    uint64_t val;                                                              \
    uint64_t mask = bitmask;                                                   \
    SET_SYSREG_BITS_BY_MASK(sysreg, val, mask);
#endif

#ifndef CLEAR_SYSREG_BITS_BY_MASK
#define CLEAR_SYSREG_BITS_BY_MASK(sysreg, val, mask)                           \
    __asm__ __volatile__(                                                      \
        "mrs %[v], "#sysreg"\n"                                                \
        "mvn %[m], %[m]\n"                                                     \
        "and %[v], %[v], %[m]\n"                                               \
        "msr "#sysreg", %[v]\n"                                                \
        : [v] "+r" (val), [m] "+r" (mask)                                      \
    )
#endif

#ifndef CLEAR_SYSREG_BITS_BY_MASK_FUNC
#define CLEAR_SYSREG_BITS_BY_MASK_FUNC(sysreg, bitmask)                        \
    uint64_t val;                                                              \
    uint64_t mask = bitmask;                                                   \
    CLEAR_SYSREG_BITS_BY_MASK(sysreg, val, mask);
#endif

#ifndef IS_SYSREG_BIT_ENABLED
#define IS_SYSREG_BIT_ENABLED(sysreg, result, lsb)                             \
    __asm__ __volatile__(                                                      \
        "mrs %[res], "#sysreg"\n"                                              \
        "lsr %[res], %[res], #"#lsb"\n"                                        \
        "and %[res], %[res], #1\n"                                             \
        : [res] "+r" (result)                                                  \
    )
#endif

#ifndef IS_SYSREG_BIT_ENABLED_FUNC
#define IS_SYSREG_BIT_ENABLED_FUNC(sysreg, lsb)                                \
    uint64_t result;                                                           \
    IS_SYSREG_BIT_ENABLED(sysreg, result, lsb);                                \
    return result;
#endif

#ifndef IS_SYSREG_BIT_DISABLED
#define IS_SYSREG_BIT_DISABLED(sysreg, result, lsb)                            \
    __asm__ __volatile__(                                                      \
        "mrs %[res], "#sysreg"\n"                                              \
        "lsr %[res], %[res], #"#lsb"\n"                                        \
        "mvn %[res], %[res]\n"                                                 \
        "and %[res], %[res], #1\n"                                             \
        : [res] "+r" (result)                                                  \
    )
#endif

#ifndef IS_SYSREG_BIT_DISABLED_FUNC
#define IS_SYSREG_BIT_DISABLED_FUNC(sysreg, lsb)                               \
    uint64_t result;                                                           \
    IS_SYSREG_BIT_DISABLED(sysreg, result, lsb);                               \
    return result;
#endif

// -----------------------------------------------------------------------------
// Vecor/SIMD/Floating Point Registers
// -----------------------------------------------------------------------------
// TODO

#endif
