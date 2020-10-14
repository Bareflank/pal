#include <pal/vmcs/eptp.h>

void test_eptp_compile(void)
{
    // Register accessors
    pal::eptp::set(0xA55A5AA5);
    auto value = pal::eptp::get();

    // Field accessors
    pal::eptp::bit_6::enable();
    pal::eptp::bit_6::enable(value);
    pal::eptp::bit_6::disable();
    pal::eptp::bit_6::disable(value);
    pal::eptp::bit_6::is_enabled();
    pal::eptp::bit_6::is_enabled(value);
    pal::eptp::bit_6::is_disabled();
    pal::eptp::bit_6::is_disabled(value);
    pal::eptp::ept_pml4_table::get();
    pal::eptp::ept_pml4_table::get(value);
    pal::eptp::ept_pml4_table::set(0x0);
    pal::eptp::ept_pml4_table::set(0x0, value);

    // Printers
    pal::eptp::print();
    pal::eptp::print(value);
    pal::eptp::bit_6::print();
    pal::eptp::bit_6::print(value);
    pal::eptp::ept_pml4_table::print();
    pal::eptp::ept_pml4_table::print(value);
}
