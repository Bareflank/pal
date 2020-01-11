#include <pal/external/edeccr.h>

uintptr_t pal_debug_base_address(void)
{ return 0; }

void test_edeccr_compile(void)
{
    // Register accessors
    pal_edeccr_set(0xA55A5AA5);
    uint32_t value = pal_edeccr_get();

    // Field accessors
    pal_edeccr_fieldset_1_nse_n__get();
    pal_edeccr_fieldset_1_nse_n__get_from_value(value);
    pal_edeccr_fieldset_1_nse_n__set(0x0);
    pal_edeccr_fieldset_1_nse_n__set_from_value(0x0, value);

    // Printers
    pal_edeccr_fieldset_1_dump();
    pal_edeccr_fieldset_1_dump_from_value(value);
    pal_edeccr_fieldset_1_nse_n__dump();
    pal_edeccr_fieldset_1_nse_n__dump_from_value(value);
}
