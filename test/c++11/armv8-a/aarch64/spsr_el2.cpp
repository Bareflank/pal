#include <pal/aarch64/spsr_el2.h>
#include <stdio.h>

void test_spsr_el2_compile(void)
{
    // Register accessors
    pal::spsr_el2::set(0xA55A5AA5);
    auto value = pal::spsr_el2::get();

    // Field accessors
    pal::spsr_el2::fieldset_1::t::enable();
    pal::spsr_el2::fieldset_1::t::enable(value);
    pal::spsr_el2::fieldset_1::t::disable();
    pal::spsr_el2::fieldset_1::t::disable(value);
    pal::spsr_el2::fieldset_1::t::is_enabled();
    pal::spsr_el2::fieldset_1::t::is_enabled(value);
    pal::spsr_el2::fieldset_1::t::is_disabled();
    pal::spsr_el2::fieldset_1::t::is_disabled(value);
    pal::spsr_el2::fieldset_1::ge::get();
    pal::spsr_el2::fieldset_1::ge::get(value);
    pal::spsr_el2::fieldset_1::ge::set(0x0);
    pal::spsr_el2::fieldset_1::ge::set(0x0, value);

    // Printers
    pal::spsr_el2::fieldset_1::print(printf);
    pal::spsr_el2::fieldset_1::print(printf, value);
    pal::spsr_el2::fieldset_1::t::print(printf);
    pal::spsr_el2::fieldset_1::t::print(printf, value);
    pal::spsr_el2::fieldset_1::ge::print(printf);
    pal::spsr_el2::fieldset_1::ge::print(printf, value);
}
