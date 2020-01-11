#include <pal/aarch64/spsr_el2.h>

void test_spsr_el2_compile(void)
{
    // Register accessors
    pal_spsr_el2_set(0xA55A5AA5);
    uint64_t value = pal_spsr_el2_get();

    // Field accessors
    pal_spsr_el2_fieldset_1_t_enable();
    pal_spsr_el2_fieldset_1_t_enable_from_value(value);
    pal_spsr_el2_fieldset_1_t_disable();
    pal_spsr_el2_fieldset_1_t_disable_from_value(value);
    pal_spsr_el2_fieldset_1_t_is_enabled();
    pal_spsr_el2_fieldset_1_t_is_enabled_from_value(value);
    pal_spsr_el2_fieldset_1_t_is_disabled();
    pal_spsr_el2_fieldset_1_t_is_disabled_from_value(value);
    pal_spsr_el2_fieldset_1_ge_get();
    pal_spsr_el2_fieldset_1_ge_get_from_value(value);
    pal_spsr_el2_fieldset_1_ge_set(0x0);
    pal_spsr_el2_fieldset_1_ge_set_from_value(0x0, value);

    // Printers
    pal_spsr_el2_fieldset_1_dump();
    pal_spsr_el2_fieldset_1_dump_from_value(value);
    pal_spsr_el2_fieldset_1_t_dump();
    pal_spsr_el2_fieldset_1_t_dump_from_value(value);
    pal_spsr_el2_fieldset_1_ge_dump();
    pal_spsr_el2_fieldset_1_ge_dump_from_value(value);
}
