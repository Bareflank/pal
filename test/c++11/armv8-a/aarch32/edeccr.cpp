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
    pal::edeccr::fieldset_1::nse_n_::get();
    pal::edeccr::fieldset_1::nse_n_::get(value);
    pal::edeccr::fieldset_1::nse_n_::set(0x0);
    pal::edeccr::fieldset_1::nse_n_::set(0x0, value);

    // Printers
    pal::edeccr::fieldset_1::dump();
    pal::edeccr::fieldset_1::dump(value);
    pal::edeccr::fieldset_1::nse_n_::dump();
    pal::edeccr::fieldset_1::nse_n_::dump(value);
}
