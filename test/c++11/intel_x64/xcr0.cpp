#include <pal/control_register/xcr0.h>

void test_xcr0_compile(void)
{
    // Register accessors
    pal::xcr0::set(0xA55A5AA5);
    auto value = pal::xcr0::get();

    // Field accessors
    pal::xcr0::sse::enable();
    pal::xcr0::sse::enable(value);
    pal::xcr0::sse::disable();
    pal::xcr0::sse::disable(value);
    pal::xcr0::sse::is_enabled();
    pal::xcr0::sse::is_enabled(value);
    pal::xcr0::sse::is_disabled();
    pal::xcr0::sse::is_disabled(value);

    // Printers
    pal::xcr0::dump();
    pal::xcr0::dump(value);
    pal::xcr0::sse::dump();
    pal::xcr0::sse::dump(value);
}
