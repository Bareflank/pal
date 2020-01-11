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
    pal::eptp::dump();
    pal::eptp::dump(value);
    pal::eptp::bit_6::dump();
    pal::eptp::bit_6::dump(value);
    pal::eptp::ept_pml4_table::dump();
    pal::eptp::ept_pml4_table::dump(value);
}
