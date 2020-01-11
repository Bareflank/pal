#include <pal/aarch32/cpacr.h>

void test_cpacr_compile(void)
{
    // Register accessors
    pal::cpacr::set(0xA55A5AA5);
    auto value = pal::cpacr::get();

    // Field accessors
    pal::cpacr::trcdis::enable();
    pal::cpacr::trcdis::enable(value);
    pal::cpacr::trcdis::disable();
    pal::cpacr::trcdis::disable(value);
    pal::cpacr::trcdis::is_enabled();
    pal::cpacr::trcdis::is_enabled(value);
    pal::cpacr::trcdis::is_disabled();
    pal::cpacr::trcdis::is_disabled(value);
    pal::cpacr::cp10::get();
    pal::cpacr::cp10::get(value);
    pal::cpacr::cp10::set(0x0);
    pal::cpacr::cp10::set(0x0, value);

    // Printers
    pal::cpacr::dump();
    pal::cpacr::dump(value);
    pal::cpacr::trcdis::dump();
    pal::cpacr::trcdis::dump(value);
    pal::cpacr::cp10::dump();
    pal::cpacr::cp10::dump(value);
}
