#include <pal/control_register/cr3.h>

void test_cr3_compile(void)
{
    // Register accessors
    pal_set_cr3(0xA55A5AA5);
    uint64_t value = pal_get_cr3();

    // Field accessors
    pal_enable_cr3_pcd();
    pal_enable_cr3_pcd_in_value(value);
    pal_disable_cr3_pcd();
    pal_disable_cr3_pcd_in_value(value);
    pal_cr3_pcd_is_enabled();
    pal_cr3_pcd_is_enabled_in_value(value);
    pal_cr3_pcd_is_disabled();
    pal_cr3_pcd_is_disabled_in_value(value);
    pal_get_cr3_page_directory_base();
    pal_get_cr3_page_directory_base_from_value(value);
    pal_set_cr3_page_directory_base(0x0);
    pal_set_cr3_page_directory_base_in_value(0x0, value);

    // Printers
    pal_print_cr3();
    pal_print_cr3_from_value(value);
    pal_print_cr3_pcd();
    pal_print_cr3_pcd_from_value(value);
    pal_print_cr3_page_directory_base();
    pal_print_cr3_page_directory_base_from_value(value);
}
