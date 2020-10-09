#include <pal/external/edeccr.h>

uintptr_t pal_debug_base_address(void)
{ return 0; }

void test_edeccr_compile(void)
{
    // Register accessors
    pal_set_edeccr(0xA55A5AA5);
    uint32_t value = pal_get_edeccr();

    // Field accessors
    pal_get_edeccr_fieldset_1_nse_n_();
    pal_get_edeccr_fieldset_1_nse_n__from_value(value);
    pal_set_edeccr_fieldset_1_nse_n_(0x0);
    pal_set_edeccr_fieldset_1_nse_n__in_value(0x0, value);

    // Printers
    pal_print_edeccr_fieldset_1();
    pal_print_edeccr_fieldset_1_from_value(value);
    pal_print_edeccr_fieldset_1_nse_n_();
    pal_print_edeccr_fieldset_1_nse_n__from_value(value);
}
