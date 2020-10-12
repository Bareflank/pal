#include <pal/vmcs/eptp.h>

void test_eptp_compile(void)
{
    // Register accessors
    pal_set_eptp(0xA55A5AA5);
    uint64_t value = pal_get_eptp();

    // Field accessors
    pal_enable_eptp_bit_6();
    pal_enable_eptp_bit_6_in_value(value);
    pal_disable_eptp_bit_6();
    pal_disable_eptp_bit_6_in_value(value);
    pal_eptp_bit_6_is_enabled();
    pal_eptp_bit_6_is_enabled_in_value(value);
    pal_eptp_bit_6_is_disabled();
    pal_eptp_bit_6_is_disabled_in_value(value);
    pal_get_eptp_ept_pml4_table();
    pal_get_eptp_ept_pml4_table_from_value(value);
    pal_set_eptp_ept_pml4_table(0x0);
    pal_set_eptp_ept_pml4_table_in_value(0x0, value);

    // Printers
    pal_print_eptp();
    pal_print_eptp_from_value(value);
    pal_print_eptp_bit_6();
    pal_print_eptp_bit_6_from_value(value);
    pal_print_eptp_ept_pml4_table();
    pal_print_eptp_ept_pml4_table_from_value(value);
}
