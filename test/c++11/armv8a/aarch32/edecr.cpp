#include <pal/external/edecr.h>
#include <stdio.h>

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
    pal::edecr::print(printf);
    pal::edecr::print(printf, value);
    pal::edecr::rce::print(printf);
    pal::edecr::rce::print(printf, value);
}
