#include <pal/aarch32/cpacr.h>

void test_cpacr_compile(void)
{
    // Register accessors
    pal_cpacr_set(0xA55A5AA5);
    uint32_t value = pal_cpacr_get();

    // Field accessors
    pal_cpacr_trcdis_enable();
    pal_cpacr_trcdis_enable_from_value(value);
    pal_cpacr_trcdis_disable();
    pal_cpacr_trcdis_disable_from_value(value);
    pal_cpacr_trcdis_is_enabled();
    pal_cpacr_trcdis_is_enabled_from_value(value);
    pal_cpacr_trcdis_is_disabled();
    pal_cpacr_trcdis_is_disabled_from_value(value);
    pal_cpacr_cp10_get();
    pal_cpacr_cp10_get_from_value(value);
    pal_cpacr_cp10_set(0x0);
    pal_cpacr_cp10_set_from_value(0x0, value);

    // Printers
    pal_cpacr_dump();
    pal_cpacr_dump_from_value(value);
    pal_cpacr_trcdis_dump();
    pal_cpacr_trcdis_dump_from_value(value);
    pal_cpacr_cp10_dump();
    pal_cpacr_cp10_dump_from_value(value);
}
