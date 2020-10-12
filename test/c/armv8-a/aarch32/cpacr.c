#include <pal/aarch32/cpacr.h>

void test_cpacr_compile(void)
{
    // Register accessors
    pal_set_cpacr(0xA55A5AA5);
    uint32_t value = pal_get_cpacr();

    // Field accessors
    pal_enable_cpacr_trcdis();
    pal_enable_cpacr_trcdis_in_value(value);
    pal_disable_cpacr_trcdis();
    pal_disable_cpacr_trcdis_in_value(value);
    pal_cpacr_trcdis_is_enabled();
    pal_cpacr_trcdis_is_enabled_in_value(value);
    pal_cpacr_trcdis_is_disabled();
    pal_cpacr_trcdis_is_disabled_in_value(value);
    pal_get_cpacr_cp10();
    pal_get_cpacr_cp10_from_value(value);
    pal_set_cpacr_cp10(0x0);
    pal_set_cpacr_cp10_in_value(0x0, value);

    // Printers
    pal_print_cpacr();
    pal_print_cpacr_from_value(value);
    pal_print_cpacr_trcdis();
    pal_print_cpacr_trcdis_from_value(value);
    pal_print_cpacr_cp10();
    pal_print_cpacr_cp10_from_value(value);
}
