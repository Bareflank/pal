/*
 * MIT License
 *
 * Copyright (c) 2020 Assured Information Security, Inc.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
*/

#ifndef LIBPAL_H
#define LIBPAL_H

#include <stdint.h>

typedef struct pal_cpuid_register_values {
    uint32_t eax;
    uint32_t ebx;
    uint32_t ecx;
    uint32_t edx;
} pal_cpuid_register_values;

/* 
 * Make sure that extern functions build for
 * C and C++ 
*/
#ifdef __cplusplus
extern "C" {
#endif

pal_cpuid_register_values pal_execute_cpuid(uint32_t eax, uint32_t ecx);

uint64_t pal_execute_rdmsr(uintptr_t ecx);

void pal_execute_wrmsr(uintptr_t addr, uint64_t value);

uint32_t pal_execute_vmread(uintptr_t addr);

void pal_execute_vmwrite(uintptr_t addr, uint64_t value);

uint64_t pal_execute_xgetbv(uintptr_t reg);

void pal_execute_xsetbv(uintptr_t reg, uint64_t value);

uint64_t pal_execute_cr0_read();

uint64_t pal_execute_cr2_read();

uint64_t pal_execute_cr3_read();

uint64_t pal_execute_cr4_read();

uint64_t pal_execute_cr8_read();

void pal_execute_cr0_write(uint64_t value);

void pal_execute_cr2_write(uint64_t value);

void pal_execute_cr3_write(uint64_t value);

void pal_execute_cr4_write(uint64_t value);

void pal_execute_cr8_write(uint64_t value);

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* LIBPAL_H */
