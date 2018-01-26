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

#define CATCH_CONFIG_MAIN
#include <stdint.h>
#include "regs.h"
#include "catch.hpp"

// -----------------------------------------------------------------------------
// Test Support
// -----------------------------------------------------------------------------

// w19 (32-bit) and x20 (64-bit) are used as test registers because they
// are required by the aarch64 calling convension to be callee-preserved
register uint32_t g_w19 asm ("w19");
register uint64_t g_x20 asm ("x20");

// The FPCR system register (floating point configuration register) is used
// for system register unit tests because it is readable and writable from EL0
// (userspace) and can be modified from within the test program without causing
// the rest of the system to become unstable.
uint64_t get_fpcr(void)
{
    uint64_t value;
    asm volatile(
        "mrs %[v], fpcr\n"
        : [v] "=r" (value)
    );
    return value;
}

void set_fpcr(uint64_t value)
{
    asm volatile(
        "msr fpcr, %[v]\n"
        : : [v] "r" (value)
    );
}

namespace test_w19
{
    inline uint32_t get(void) noexcept { GET_REG32_FUNC(w19) }
    inline void set(uint32_t val) noexcept { SET_REG32_FUNC(w19, val) }
}

namespace test_x20
{
    inline uint64_t get(void) noexcept { GET_REG64_FUNC(x20) }
    inline void set(uint64_t val) noexcept { SET_REG64_FUNC(x20, val) }
}

namespace test_fpcr
{
    inline uint64_t get(void) noexcept { GET_SYSREG_FUNC(fpcr) }
    inline void set(uint64_t val) noexcept { SET_SYSREG_BY_VALUE_FUNC(fpcr, val) }

    namespace ioe
    {
        inline uint64_t is_enabled() noexcept { IS_SYSREG_BIT_ENABLED_FUNC(fpcr, 8) }
        inline uint64_t is_enabled(uint64_t fpcr_val) noexcept { IS_BIT_ENABLED_FUNC(fpcr_val, 8) }
        inline uint64_t is_disabled() noexcept { IS_SYSREG_BIT_DISABLED_FUNC(fpcr, 8) }
        inline uint64_t is_disabled(uint64_t fpcr_val) noexcept { IS_BIT_DISABLED_FUNC(fpcr_val, 8) }
        inline void enable() noexcept { SET_SYSREG_BITS_BY_MASK_FUNC(fpcr, 0x100) }
        inline uint64_t enable(uint64_t fpcr_val) noexcept { SET_BITS_BY_MASK_FUNC(fpcr_val, 0x100) }
        inline void disable() noexcept { CLEAR_SYSREG_BITS_BY_MASK_FUNC(fpcr, 0x100) }
        inline uint64_t disable(uint64_t fpcr_val) noexcept { CLEAR_BITS_BY_MASK_FUNC(fpcr_val, 0x100) }
    }

    namespace len
    {
        inline uint64_t get() noexcept { GET_SYSREG_FIELD_FUNC(fpcr, 0x70000, 16) }
        inline uint64_t get(uint64_t fpcr_val) noexcept { GET_BITFIELD_FUNC(fpcr_val, 0x70000, 16) }
        inline void set(uint64_t value) noexcept { SET_SYSREG_BITS_BY_VALUE_FUNC(fpcr, value, 0x70000, 16) }
        inline uint64_t set(uint64_t fpcr_val, uint64_t value) noexcept { SET_BITS_BY_VALUE_FUNC(fpcr_val, value, 0x70000, 16) }
    }
}

// -----------------------------------------------------------------------------
// Test Cases
// -----------------------------------------------------------------------------

TEST_CASE("GET_REG32")
{
    uint32_t val;

    g_w19 = 0;
    GET_REG32(w19, val);
    CHECK(val == 0);

    g_w19 = 1;
    GET_REG32(w19, val);
    CHECK(val == 1);

    g_w19 = 0xf00dbeef;
    GET_REG32(w19, val);
    CHECK(val == 0xf00dbeef);

    g_w19 = 0xffffffff;
    GET_REG32(w19, val);
    CHECK(val == 0xffffffff);
}

TEST_CASE("GET_REG32_FUNC")
{
    g_w19 = 0xf00dbeef;
    uint32_t result = test_w19::get();
    CHECK(result == 0xf00dbeef);
    g_w19 = 0;
}

TEST_CASE("GET_REG64")
{
    uint64_t val;

    g_x20 = 0;
    GET_REG64(x20, val);
    CHECK(val == 0);

    g_x20 = 1;
    GET_REG64(x20, val);
    CHECK(val == 1);

    g_x20 = 0xdeadf00dbeefd00d;
    GET_REG64(x20, val);
    CHECK(val == 0xdeadf00dbeefd00d);

    g_x20 = 0xffffffffffffffff;
    GET_REG64(x20, val);
    CHECK(val == 0xffffffffffffffff);
}

TEST_CASE("GET_REG64_FUNC")
{
    g_x20 = 0xdeadf00dbeefd00d;
    uint64_t result = test_x20::get();
    CHECK(result == 0xdeadf00dbeefd00d);
    g_x20 = 0;
}

TEST_CASE("SET_REG32")
{
    uint32_t val;

    SET_REG32(w19, 0);
    val = g_w19;
    CHECK(val == 0);

    SET_REG32(w19, 1);
    val = g_w19;
    CHECK(val == 1);

    SET_REG32(w19, 0xf00dbeef);
    val = g_w19;
    CHECK(val == 0xf00dbeef);

    SET_REG32(w19, 0xffffffff);
    val = g_w19;
    CHECK(val == 0xffffffff);
}

TEST_CASE("SET_REG32_FUNC")
{
    test_w19::set(0xc001d00d);
    uint32_t result = g_w19;
    CHECK(result == 0xc001d00d);
    g_w19 = 0;
}

TEST_CASE("SET_REG64")
{
    uint64_t val;

    SET_REG64(x20, 0);
    val = g_x20;
    CHECK(val == 0);

    SET_REG64(x20, 1);
    val = g_x20;
    CHECK(val == 1);

    SET_REG64(x20, 0xdeadf00dbeefd00d);
    val = g_x20;
    CHECK(val == 0xdeadf00dbeefd00d);

    SET_REG64(x20, 0xffffffffffffffff);
    val = g_x20;
    CHECK(val == 0xffffffffffffffff);
}

TEST_CASE("SET_REG64_FUNC")
{
    test_x20::set(0xbadc0feecafebabe);
    uint64_t result = g_x20;
    CHECK(result == 0xbadc0feecafebabe);
    g_x20 = 0;
}

TEST_CASE("GET_BITFIELD")
{
    uint64_t fpcr_val, mask;

    fpcr_val = 0;
    mask = 0;
    GET_BITFIELD(fpcr_val, mask, 16);
    CHECK(fpcr_val == 0);

    fpcr_val = 0;
    mask = 1;
    GET_BITFIELD(fpcr_val, mask, 0);
    CHECK(fpcr_val == 0);

    fpcr_val = 0;
    mask = 0xffffffffffffffff;
    GET_BITFIELD(fpcr_val, mask, 1);
    CHECK(fpcr_val == 0);

    fpcr_val = 1;
    mask = 1;
    GET_BITFIELD(fpcr_val, mask, 0);
    CHECK(fpcr_val == 1);

    fpcr_val = 0xffffffffffffffff;
    mask = 1;
    GET_BITFIELD(fpcr_val, mask, 0);
    CHECK(fpcr_val == 1);

    fpcr_val = 0xffffffffffffffff;
    mask = 0x400;
    GET_BITFIELD(fpcr_val, mask, 10);
    CHECK(fpcr_val == 1);

    fpcr_val = 0xffffffffffffffff;
    mask = 0x8000000000000000;
    GET_BITFIELD(fpcr_val, mask, 63);
    CHECK(fpcr_val == 1);

    fpcr_val = 0xffffffffffffffff;
    mask = 0xf0000;
    GET_BITFIELD(fpcr_val, mask, 16);
    CHECK(fpcr_val == 0xf);

    fpcr_val = 0x70000;
    mask = 0xf0000;
    GET_BITFIELD(fpcr_val, mask, 16);
    CHECK(fpcr_val == 7);

    fpcr_val = 0x100;
    mask = 0x100;
    GET_BITFIELD(fpcr_val, mask, 8);
    CHECK(fpcr_val == 1);

    fpcr_val = 0xffffffffffffffff;
    mask = 0xffffffffffffffff;
    GET_BITFIELD(fpcr_val, mask, 0);
    CHECK(fpcr_val == 0xffffffffffffffff);

    fpcr_val = 0xff00;
    mask = 0xff00;
    GET_BITFIELD(fpcr_val, mask, 0);
    CHECK(fpcr_val == 0xff00);
}

TEST_CASE("GET_BITFIELD_FUNC")
{
    uint64_t fpcr_val, result;

    fpcr_val = 0;
    result = test_fpcr::len::get(fpcr_val);
    CHECK(result == 0);

    fpcr_val = 0x70000;
    result = test_fpcr::len::get(fpcr_val);
    CHECK(result == 7);

    fpcr_val = 0x60000;
    result = test_fpcr::len::get(fpcr_val);
    CHECK(result == 6);

    fpcr_val = 0x50000;
    result = test_fpcr::len::get(fpcr_val);
    CHECK(result == 5);

    fpcr_val = 0x40000;
    result = test_fpcr::len::get(fpcr_val);
    CHECK(result == 4);

    fpcr_val = 0x30000;
    result = test_fpcr::len::get(fpcr_val);
    CHECK(result == 3);

    fpcr_val = 0x20000;
    result = test_fpcr::len::get(fpcr_val);
    CHECK(result == 2);

    fpcr_val = 0x10000;
    result = test_fpcr::len::get(fpcr_val);
    CHECK(result == 1);

    fpcr_val = 0xffffffffffffffff;
    result = test_fpcr::len::get(fpcr_val);
    CHECK(result == 7);
}

TEST_CASE("SET_BITS_BY_VALUE")
{
    uint64_t fpcr_val, val, mask;

    fpcr_val = 0;
    val = 0;
    mask = 0;
    SET_BITS_BY_VALUE(fpcr_val, val, mask, 0);
    CHECK(fpcr_val == 0);

    fpcr_val = 0;
    val = 1;
    mask = 1;
    SET_BITS_BY_VALUE(fpcr_val, val, mask, 0);
    CHECK(fpcr_val == 1);

    fpcr_val = 0;
    val = 1;
    mask = 0x2;
    SET_BITS_BY_VALUE(fpcr_val, val, mask, 1);
    CHECK(fpcr_val == 0x2);

    fpcr_val = 0;
    val = 0xf;
    mask = 0xf;
    SET_BITS_BY_VALUE(fpcr_val, val, mask, 0);
    CHECK(fpcr_val == 0xf);

    fpcr_val = 0;
    val = 8;
    mask = 0xf;
    SET_BITS_BY_VALUE(fpcr_val, val, mask, 0);
    CHECK(fpcr_val == 8);

    fpcr_val = 0;
    val = 0xffffff;
    mask = 0xffffff00;
    SET_BITS_BY_VALUE(fpcr_val, val, mask, 8);
    CHECK(fpcr_val == 0xffffff00);

    fpcr_val = 0;
    val = 0xffffffff;
    mask = 0xffffffff;
    SET_BITS_BY_VALUE(fpcr_val, val, mask, 0);
    CHECK(fpcr_val == 0xffffffff);

    fpcr_val = 0;
    val = 0xffffffffffffffff;
    mask = 0xffffffffffffffff;
    SET_BITS_BY_VALUE(fpcr_val, val, mask, 0);
    CHECK(fpcr_val == 0xffffffffffffffff);

    fpcr_val = 0;
    val = 0xffffffffffffffff;
    mask = 0xff00;
    SET_BITS_BY_VALUE(fpcr_val, val, mask, 0);
    CHECK(fpcr_val == 0xff00);
}

TEST_CASE("SET_BITS_BY_VALUE_FUNC")
{
    uint64_t fpcr_val, result;

    fpcr_val = 0;
    result = test_fpcr::len::set(fpcr_val, 0);
    CHECK(result == 0);

    fpcr_val = 0;
    result = test_fpcr::len::set(fpcr_val, 1);
    CHECK(result == 0x10000);

    fpcr_val = 0;
    result = test_fpcr::len::set(fpcr_val, 7);
    CHECK(result == 0x70000);

    fpcr_val = 0xffffffffffffffff;
    result = test_fpcr::len::set(fpcr_val, 0);
    CHECK(result == 0xfffffffffff8ffff);

    fpcr_val = 0xffffffffffffffff;
    result = test_fpcr::len::set(fpcr_val, 7);
    CHECK(result == 0xffffffffffffffff);
}

TEST_CASE("SET_BITS_BY_MASK")
{
    uint64_t value, mask;

    value = 0;
    mask = 0;
    SET_BITS_BY_MASK(value, mask);
    CHECK(value == 0);

    value = 0;
    mask = 1;
    SET_BITS_BY_MASK(value, mask);
    CHECK(value == 1);

    value = 0;
    mask = 0xf;
    SET_BITS_BY_MASK(value, mask);
    CHECK(value == 0xf);

    value = 0;
    mask = 0x500;
    SET_BITS_BY_MASK(value, mask);
    CHECK(value == 0x500);

    value = 0;
    mask = 0xf0000;
    SET_BITS_BY_MASK(value, mask);
    CHECK(value == 0xf0000);

    value = 0;
    mask = 0xffffffffffffffff;
    SET_BITS_BY_MASK(value, mask);
    CHECK(value == 0xffffffffffffffff);
}

TEST_CASE("SET_BITS_BY_MASK_FUNC")
{
    uint64_t fpcr_val, result;

    fpcr_val = 0;
    result = test_fpcr::ioe::enable(fpcr_val);
    CHECK(result == 0x100);
    result = test_fpcr::ioe::enable(result);
    CHECK(result == 0x100);

    fpcr_val = 0xfffffffffffffeff;
    result = test_fpcr::ioe::enable(fpcr_val);
    CHECK(result == 0xffffffffffffffff);
}

TEST_CASE("CLEAR_BITS_BY_MASK")
{
    uint64_t value, mask;

    value = 0;
    mask = 0;
    CLEAR_BITS_BY_MASK(value, mask);
    CHECK(value == 0);

    value = 0;
    mask = 1;
    CLEAR_BITS_BY_MASK(value, mask);
    CHECK(value == 0);

    value = 1;
    mask = 1;
    CLEAR_BITS_BY_MASK(value, mask);
    CHECK(value == 0);

    value = 1;
    mask = 1;
    CLEAR_BITS_BY_MASK(value, mask);
    CHECK(value == 0);

    value = 7;
    mask = 2;
    CLEAR_BITS_BY_MASK(value, mask);
    CHECK(value == 5);

    value = 0xffffffffffffffff;
    mask = 1;
    CLEAR_BITS_BY_MASK(value, mask);
    CHECK(value == 0xfffffffffffffffe);

    value = 0xffffffffffffffff;
    mask = 0x00000000ff000000;
    CLEAR_BITS_BY_MASK(value, mask);
    CHECK(value == 0xffffffff00ffffff);

    value = 0xffffffffffffffff;
    mask = 0xffffffffffffffff;
    CLEAR_BITS_BY_MASK(value, mask);
    CHECK(value == 0);
}

TEST_CASE("CLEAR_BITS_BY_MASK_FUNC")
{
    uint64_t fpcr_val, result;

    fpcr_val = 0;
    result = test_fpcr::ioe::disable(fpcr_val);
    CHECK(result == 0);

    fpcr_val = 0xffffffffffffffff;
    result = test_fpcr::ioe::disable(fpcr_val);
    CHECK(result == 0xfffffffffffffeff);
    result = test_fpcr::ioe::disable(result);
    CHECK(result == 0xfffffffffffffeff);
}

TEST_CASE("IS_BIT_ENABLED")
{
    uint64_t result;

    g_w19 = 0;
    IS_BIT_ENABLED(g_w19, result, 0);
    CHECK(result == 0);

    g_x20 = 0;
    IS_BIT_ENABLED(g_x20, result, 0);
    CHECK(result == 0);

    g_w19 = 1;
    IS_BIT_ENABLED(g_w19, result, 0);
    CHECK(result == 1);
    IS_BIT_ENABLED(g_w19, result, 1);
    CHECK(result == 0);

    g_x20 = 1;
    IS_BIT_ENABLED(g_x20, result, 0);
    CHECK(result == 1);
    IS_BIT_ENABLED(g_x20, result, 1);
    CHECK(result == 0);

    g_w19 = 0x500;
    IS_BIT_ENABLED(g_w19, result, 8);
    CHECK(result == 1);
    IS_BIT_ENABLED(g_w19, result, 9);
    CHECK(result == 0);
    IS_BIT_ENABLED(g_w19, result, 10);
    CHECK(result == 1);

    g_x20 = 0x500;
    IS_BIT_ENABLED(g_x20, result, 8);
    CHECK(result == 1);
    IS_BIT_ENABLED(g_x20, result, 9);
    CHECK(result == 0);
    IS_BIT_ENABLED(g_x20, result, 10);
    CHECK(result == 1);

    g_w19 = 0xffffffff;
    IS_BIT_ENABLED(g_w19, result, 0);
    CHECK(result == 1);
    IS_BIT_ENABLED(g_w19, result, 1);
    CHECK(result == 1);
    IS_BIT_ENABLED(g_w19, result, 18);
    CHECK(result == 1);
    IS_BIT_ENABLED(g_w19, result, 31);
    CHECK(result == 1);

    g_x20 = 0xffffffffffffffff;
    IS_BIT_ENABLED(g_x20, result, 0);
    CHECK(result == 1);
    IS_BIT_ENABLED(g_x20, result, 1);
    CHECK(result == 1);
    IS_BIT_ENABLED(g_x20, result, 27);
    CHECK(result == 1);
    IS_BIT_ENABLED(g_x20, result, 63);
    CHECK(result == 1);
}

TEST_CASE("IS_BIT_ENABLED_FUNC")
{
    uint64_t fpcr_val, result;

    fpcr_val = 0x100;
    result = test_fpcr::ioe::is_enabled(fpcr_val);
    CHECK(result == 1);

    fpcr_val = 0;
    result = test_fpcr::ioe::is_enabled(fpcr_val);
    CHECK(result == 0);

    fpcr_val = 0xfffffffffffffeff;
    result = test_fpcr::ioe::is_enabled(fpcr_val);
    CHECK(result == 0);
}

TEST_CASE("IS_BIT_DISABLED")
{
    uint64_t result;

    g_w19 = 0;
    IS_BIT_DISABLED(g_w19, result, 0);
    CHECK(result == 1);

    g_x20 = 0;
    IS_BIT_DISABLED(g_x20, result, 0);
    CHECK(result == 1);

    g_w19 = 1;
    IS_BIT_DISABLED(g_w19, result, 0);
    CHECK(result == 0);
    IS_BIT_DISABLED(g_w19, result, 1);
    CHECK(result == 1);

    g_x20 = 1;
    IS_BIT_DISABLED(g_x20, result, 0);
    CHECK(result == 0);
    IS_BIT_DISABLED(g_x20, result, 1);
    CHECK(result == 1);

    g_w19 = 0x500;
    IS_BIT_DISABLED(g_w19, result, 8);
    CHECK(result == 0);
    IS_BIT_DISABLED(g_w19, result, 9);
    CHECK(result == 1);
    IS_BIT_DISABLED(g_w19, result, 10);
    CHECK(result == 0);

    g_x20 = 0x500;
    IS_BIT_DISABLED(g_x20, result, 8);
    CHECK(result == 0);
    IS_BIT_DISABLED(g_x20, result, 9);
    CHECK(result == 1);
    IS_BIT_DISABLED(g_x20, result, 10);
    CHECK(result == 0);

    g_w19 = 0xffffffff;
    IS_BIT_DISABLED(g_w19, result, 0);
    CHECK(result == 0);
    IS_BIT_DISABLED(g_w19, result, 1);
    CHECK(result == 0);
    IS_BIT_DISABLED(g_w19, result, 18);
    CHECK(result == 0);
    IS_BIT_DISABLED(g_w19, result, 31);
    CHECK(result == 0);

    g_x20 = 0xffffffffffffffff;
    IS_BIT_DISABLED(g_x20, result, 0);
    CHECK(result == 0);
    IS_BIT_DISABLED(g_x20, result, 1);
    CHECK(result == 0);
    IS_BIT_DISABLED(g_x20, result, 27);
    CHECK(result == 0);
    IS_BIT_DISABLED(g_x20, result, 63);
    CHECK(result == 0);
}

TEST_CASE("IS_BIT_DISABLED_FUNC")
{
    uint64_t fpcr_val, result;

    fpcr_val = 0x100;
    result = test_fpcr::ioe::is_disabled(fpcr_val);
    CHECK(result == 0);

    fpcr_val = 0;
    result = test_fpcr::ioe::is_disabled(fpcr_val);
    CHECK(result == 1);

    fpcr_val = 0xfffffffffffffeff;
    result = test_fpcr::ioe::is_disabled(fpcr_val);
    CHECK(result == 1);
}

TEST_CASE("GET_SYSREG")
{
    uint64_t val, previous_val;
    const uint64_t expected_val = 0x100;

    previous_val = get_fpcr();
    set_fpcr(expected_val);

    GET_SYSREG(fpcr, val);
    CHECK(val == expected_val);

    set_fpcr(previous_val);
}

TEST_CASE("GET_SYSREG_FUNC")
{
    uint64_t previous_fpcr_val = get_fpcr();
    set_fpcr(0x50100);
    uint64_t result = test_fpcr::get();
    CHECK(result == 0x50100);
    set_fpcr(previous_fpcr_val);
}

TEST_CASE("GET_SYSREG_FIELD")
{
    uint64_t val, previous_val;

    previous_val = get_fpcr();

    // Set fpcr.ioe = '1', fpcr.len = '101', and all other bits to '0'
    set_fpcr(0x50100);

    // fpcr.ioe
    GET_SYSREG_FIELD(fpcr, val, 0x100, 8);
    CHECK(val == 1);

    // fpcr.DZE
    GET_SYSREG_FIELD(fpcr, val, 0x200, 9);
    CHECK(val == 0);

    // fpcr.res0 [7:0]
    GET_SYSREG_FIELD(fpcr, val, 0xff, 0);
    CHECK(val == 0);

    // fpcr.len [18:16]
    GET_SYSREG_FIELD(fpcr, val, 0x50000, 16);
    CHECK(val == 0b101);

    // fpcr.res0 [31:27]
    GET_SYSREG_FIELD(fpcr, val, 0xf8000000, 27);
    CHECK(val == 0);

    set_fpcr(previous_val);
}

TEST_CASE("GET_SYSREG_FIELD_FUNC")
{
    uint64_t result;
    uint64_t previous_fpcr_val = get_fpcr();

    set_fpcr(0x100);
    result = test_fpcr::len::get();
    CHECK(result == 0);

    set_fpcr(0x50100);
    result = test_fpcr::len::get();
    CHECK(result == 5);

    set_fpcr(0x70000);
    result = test_fpcr::len::get();
    CHECK(result == 7);

    set_fpcr(previous_fpcr_val);
}

TEST_CASE("SET_SYSREG_BY_VALUE")
{
    uint64_t val, previous_val;
    previous_val = get_fpcr();

    SET_SYSREG_BY_VALUE(fpcr, 0);
    val = get_fpcr();
    CHECK(val == 0);

    // One valid bit on
    SET_SYSREG_BY_VALUE(fpcr, 0x100);
    val = get_fpcr();
    CHECK(val == 0x100);

    set_fpcr(previous_val);
}

TEST_CASE("SET_SYSREG_BY_VALUE_FUNC")
{
    uint64_t previous_fpcr_val = get_fpcr();
    test_fpcr::set(0x50100);
    uint64_t result = get_fpcr();
    CHECK(result == 0x50100);
    set_fpcr(previous_fpcr_val);
}

TEST_CASE("SET_SYSREG_BITS_BY_VALUE")
{
    uint64_t reg_val, new_val, old_val, mask, previous_val = 0;
    previous_val = get_fpcr();

    // Set fpcr.ioe [8] to '1'
    set_fpcr(0);
    new_val = 1;
    mask = 0x100;
    SET_SYSREG_BITS_BY_VALUE(fpcr, new_val, old_val, mask, 8);
    reg_val = get_fpcr();
    CHECK(reg_val == 0x100);

    // Set fpcr.len [18:16] to '101'
    set_fpcr(0);
    new_val = 5;
    mask = 0x70000;
    SET_SYSREG_BITS_BY_VALUE(fpcr, new_val, old_val, mask, 16);
    reg_val = get_fpcr();
    CHECK(reg_val == 0x50000);

    set_fpcr(previous_val);
}

TEST_CASE("SET_SYSREG_BITS_BY_VALUE_FUNC")
{
    uint64_t result;
    uint64_t previous_fpcr_val = get_fpcr();
    set_fpcr(0);

    test_fpcr::len::set(7);
    result = get_fpcr();
    CHECK(result == 0x70000);

    test_fpcr::len::set(5);
    result = get_fpcr();
    CHECK(result == 0x50000);

    test_fpcr::len::set(0);
    result = get_fpcr();
    CHECK(result == 0);

    test_fpcr::len::set(0xffffffff);
    result = get_fpcr();
    CHECK(result == 0x70000);

    set_fpcr(previous_fpcr_val);
}

TEST_CASE("SET_SYSREG_BITS_BY_MASK")
{
    uint64_t val, previous_val, mask;
    previous_val = get_fpcr();

    // Set fpcr.ioe [8]
    set_fpcr(0);
    mask = 0x100;
    SET_SYSREG_BITS_BY_MASK(fpcr, val, mask);
    val = get_fpcr();
    CHECK(val == 0x100);

    // Set fpcr.len [18:16]
    set_fpcr(0);
    mask = 0x70000;
    SET_SYSREG_BITS_BY_MASK(fpcr, val, mask);
    val = get_fpcr();
    CHECK(val == 0x70000);

    set_fpcr(previous_val);
}

TEST_CASE("SET_SYSREG_BITS_BY_MASK_FUNC")
{
    uint64_t result;
    uint64_t previous_fpcr_val = get_fpcr();
    set_fpcr(0);

    test_fpcr::ioe::enable();
    result = get_fpcr();
    CHECK(result == 0x100);

    test_fpcr::ioe::enable();
    result = get_fpcr();
    CHECK(result == 0x100);

    set_fpcr(previous_fpcr_val);
}

TEST_CASE("CLEAR_SYSREG_BITS_BY_MASK")
{
    uint64_t val, previous_val, mask;
    previous_val = get_fpcr();

    // Clear fpcr.ioe [8]
    set_fpcr(0x100);
    mask = 0x100;
    CLEAR_SYSREG_BITS_BY_MASK(fpcr, val, mask);
    val = get_fpcr();
    CHECK(val == 0);

    // Clear fpcr.len [18:16]
    set_fpcr(0x70000);
    mask = 0x70000;
    CLEAR_SYSREG_BITS_BY_MASK(fpcr, val, mask);
    val = get_fpcr();
    CHECK(val == 0);

    set_fpcr(previous_val);
}

TEST_CASE("CLEAR_SYSREG_BITS_BY_MASK_FUNC")
{
    uint64_t result;
    uint64_t previous_fpcr_val = get_fpcr();
    set_fpcr(0x100);

    test_fpcr::ioe::disable();
    result = get_fpcr();
    CHECK(result == 0);

    test_fpcr::ioe::disable();
    result = get_fpcr();
    CHECK(result == 0);

    set_fpcr(previous_fpcr_val);
}

TEST_CASE("IS_SYSREG_BIT_ENABLED")
{
    uint64_t result, previous_val;
    previous_val = get_fpcr();

    // Set fpcr.ioe = '1', fpcr.len = '101', and all other bits to '0'
    set_fpcr(0x50100);

    IS_SYSREG_BIT_ENABLED(fpcr, result, 8);
    CHECK(result == 1);

    IS_SYSREG_BIT_ENABLED(fpcr, result, 16);
    CHECK(result == 1);

    IS_SYSREG_BIT_ENABLED(fpcr, result, 18);
    CHECK(result == 1);

    IS_SYSREG_BIT_ENABLED(fpcr, result, 9);
    CHECK(result == 0);

    IS_SYSREG_BIT_ENABLED(fpcr, result, 17);
    CHECK(result == 0);
}

TEST_CASE("IS_SYSREG_BIT_ENABLED_FUNC")
{
    bool result;
    uint64_t previous_fpcr_val = get_fpcr();

    set_fpcr(0x100);
    result = test_fpcr::ioe::is_enabled();
    CHECK(result == true);

    set_fpcr(0);
    result = test_fpcr::ioe::is_enabled();
    CHECK(result == false);

    set_fpcr(previous_fpcr_val);
}

TEST_CASE("IS_SYSREG_BIT_DISABLED")
{
    uint64_t result, previous_val;
    previous_val = get_fpcr();

    // Set fpcr.ioe = '1', fpcr.len = '101', and all other bits to '0'
    set_fpcr(0x50100);

    IS_SYSREG_BIT_DISABLED(fpcr, result, 8);
    CHECK(result == 0);

    IS_SYSREG_BIT_DISABLED(fpcr, result, 16);
    CHECK(result == 0);

    IS_SYSREG_BIT_DISABLED(fpcr, result, 18);
    CHECK(result == 0);

    IS_SYSREG_BIT_DISABLED(fpcr, result, 9);
    CHECK(result == 1);

    IS_SYSREG_BIT_DISABLED(fpcr, result, 17);
    CHECK(result == 1);
}

TEST_CASE("IS_SYSREG_BIT_DISABLED_FUNC")
{
    bool result;
    uint64_t previous_fpcr_val = get_fpcr();

    set_fpcr(0x100);
    result = test_fpcr::ioe::is_disabled();
    CHECK(result == false);

    set_fpcr(0);
    result = test_fpcr::ioe::is_disabled();
    CHECK(result == true);

    set_fpcr(previous_fpcr_val);
}
