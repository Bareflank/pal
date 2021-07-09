#include <pal/external/edeccr.h>

namespace pal
{
    uintptr_t debug_base_address(void)
    { return 0; }
}

void test_edeccr_compile(void)
{
    // Register accessors
    pal::edeccr::set(0xA55A5AA5);
    auto value = pal::edeccr::get();

    // Field accessors
    pal::edeccr::fieldset_1::nse_n::get();
    pal::edeccr::fieldset_1::nse_n::get(value);
    pal::edeccr::fieldset_1::nse_n::set(0x0);
    pal::edeccr::fieldset_1::nse_n::set(0x0, value);

    // Printers
    pal::edeccr::fieldset_1::print();
    pal::edeccr::fieldset_1::print(value);
    pal::edeccr::fieldset_1::nse_n::print();
    pal::edeccr::fieldset_1::nse_n::print(value);
}
