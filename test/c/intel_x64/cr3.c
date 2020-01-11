#include <pal/control_register/cr3.h>

void test_cr3_compile(void)
{
    // Register accessors
    pal_cr3_set(0xA55A5AA5);
    uint64_t value = pal_cr3_get();

    // Field accessors
    pal_cr3_pcd_enable();
    pal_cr3_pcd_enable_from_value(value);
    pal_cr3_pcd_disable();
    pal_cr3_pcd_disable_from_value(value);
    pal_cr3_pcd_is_enabled();
    pal_cr3_pcd_is_enabled_from_value(value);
    pal_cr3_pcd_is_disabled();
    pal_cr3_pcd_is_disabled_from_value(value);
    pal_cr3_page_directory_base_get();
    pal_cr3_page_directory_base_get_from_value(value);
    pal_cr3_page_directory_base_set(0x0);
    pal_cr3_page_directory_base_set_from_value(0x0, value);

    // Printers
    pal_cr3_dump();
    pal_cr3_dump_from_value(value);
    pal_cr3_pcd_dump();
    pal_cr3_pcd_dump_from_value(value);
    pal_cr3_page_directory_base_dump();
    pal_cr3_page_directory_base_dump_from_value(value);
}
