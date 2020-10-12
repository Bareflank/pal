#include <pal/aarch64/spsr_el2.h>

void test_spsr_el2_compile(void)
{
    // Register accessors
    pal_set_spsr_el2(0xA55A5AA5);
    uint64_t value = pal_get_spsr_el2();

    // Field accessors
    pal_enable_spsr_el2_fieldset_1_t();
    pal_enable_spsr_el2_fieldset_1_t_in_value(value);
    pal_disable_spsr_el2_fieldset_1_t();
    pal_disable_spsr_el2_fieldset_1_t_in_value(value);
    pal_spsr_el2_fieldset_1_t_is_enabled();
    pal_spsr_el2_fieldset_1_t_is_enabled_in_value(value);
    pal_spsr_el2_fieldset_1_t_is_disabled();
    pal_spsr_el2_fieldset_1_t_is_disabled_in_value(value);
    pal_get_spsr_el2_fieldset_1_ge();
    pal_get_spsr_el2_fieldset_1_ge_from_value(value);
    pal_set_spsr_el2_fieldset_1_ge(0x0);
    pal_set_spsr_el2_fieldset_1_ge_in_value(0x0, value);

    // Printers
    pal_print_spsr_el2_fieldset_1();
    pal_print_spsr_el2_fieldset_1_from_value(value);
    pal_print_spsr_el2_fieldset_1_t();
    pal_print_spsr_el2_fieldset_1_t_from_value(value);
    pal_print_spsr_el2_fieldset_1_ge();
    pal_print_spsr_el2_fieldset_1_ge_from_value(value);
}
