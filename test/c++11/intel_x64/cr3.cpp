#include <pal/control_register/cr3.h>

void test_cr3_compile(void)
{
    // Register accessors
    pal::cr3::set(0xA55A5AA5);
    auto value = pal::cr3::get();

    // Field accessors
    pal::cr3::pcd::enable();
    pal::cr3::pcd::enable(value);
    pal::cr3::pcd::disable();
    pal::cr3::pcd::disable(value);
    pal::cr3::pcd::is_enabled();
    pal::cr3::pcd::is_enabled(value);
    pal::cr3::pcd::is_disabled();
    pal::cr3::pcd::is_disabled(value);
    pal::cr3::page_directory_base::get();
    pal::cr3::page_directory_base::get(value);
    pal::cr3::page_directory_base::set(0x0);
    pal::cr3::page_directory_base::set(0x0, value);

    // Printers
    pal::cr3::dump();
    pal::cr3::dump(value);
    pal::cr3::pcd::dump();
    pal::cr3::pcd::dump(value);
    pal::cr3::page_directory_base::dump();
    pal::cr3::page_directory_base::dump(value);
}
