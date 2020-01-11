#include <pal/vmcs/eptp.h>

void test_eptp_compile(void)
{
    // Register accessors
    pal_eptp_set(0xA55A5AA5);
    uint64_t value = pal_eptp_get();

    // Field accessors
    pal_eptp_bit_6_enable();
    pal_eptp_bit_6_enable_from_value(value);
    pal_eptp_bit_6_disable();
    pal_eptp_bit_6_disable_from_value(value);
    pal_eptp_bit_6_is_enabled();
    pal_eptp_bit_6_is_enabled_from_value(value);
    pal_eptp_bit_6_is_disabled();
    pal_eptp_bit_6_is_disabled_from_value(value);
    pal_eptp_ept_pml4_table_get();
    pal_eptp_ept_pml4_table_get_from_value(value);
    pal_eptp_ept_pml4_table_set(0x0);
    pal_eptp_ept_pml4_table_set_from_value(0x0, value);

    // Printers
    pal_eptp_dump();
    pal_eptp_dump_from_value(value);
    pal_eptp_bit_6_dump();
    pal_eptp_bit_6_dump_from_value(value);
    pal_eptp_ept_pml4_table_dump();
    pal_eptp_ept_pml4_table_dump_from_value(value);
}
