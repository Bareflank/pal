#include <pal/external/edecr.h>

void test_edecr_compile(void)
{
    // Register accessors
    pal::edecr::set(0xA55A5AA5);
    auto value = pal::edecr::get();

    // Field accessors
    pal::edecr::rce::enable();
    pal::edecr::rce::enable(value);
    pal::edecr::rce::disable();
    pal::edecr::rce::disable(value);
    pal::edecr::rce::is_enabled();
    pal::edecr::rce::is_enabled(value);
    pal::edecr::rce::is_disabled();
    pal::edecr::rce::is_disabled(value);

    // Printers
    pal::edecr::print();
    pal::edecr::print(value);
    pal::edecr::rce::print();
    pal::edecr::rce::print(value);
}
