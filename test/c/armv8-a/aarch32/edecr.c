#include <pal/external/edecr.h>

void test_edecr_compile(void)
{
    // Register accessors
    pal_edecr_set(0xA55A5AA5);
    uint32_t value = pal_edecr_get();

    // Field accessors
    pal_edecr_rce_enable();
    pal_edecr_rce_enable_from_value(value);
    pal_edecr_rce_disable();
    pal_edecr_rce_disable_from_value(value);
    pal_edecr_rce_is_enabled();
    pal_edecr_rce_is_enabled_from_value(value);
    pal_edecr_rce_is_disabled();
    pal_edecr_rce_is_disabled_from_value(value);

    // Printers
    pal_edecr_dump();
    pal_edecr_dump_from_value(value);
    pal_edecr_rce_dump();
    pal_edecr_rce_dump_from_value(value);
}
