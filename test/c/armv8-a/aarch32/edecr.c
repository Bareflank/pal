#include <pal/external/edecr.h>

void test_edecr_compile(void)
{
    // Register accessors
    pal_set_edecr(0xA55A5AA5);
    uint32_t value = pal_get_edecr();

    // Field accessors
    pal_enable_edecr_rce();
    pal_enable_edecr_rce_in_value(value);
    pal_disable_edecr_rce();
    pal_disable_edecr_rce_in_value(value);
    pal_edecr_rce_is_enabled();
    pal_edecr_rce_is_enabled_in_value(value);
    pal_edecr_rce_is_disabled();
    pal_edecr_rce_is_disabled_in_value(value);

    // Printers
    pal_print_edecr();
    pal_print_edecr_from_value(value);
    pal_print_edecr_rce();
    pal_print_edecr_rce_from_value(value);
}
