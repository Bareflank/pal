#include <pal/control_register/xcr0.h>

void test_xcr0_compile(void)
{
    // Register accessors
    pal_xcr0_set(0xA55A5AA5);
    uint64_t value = pal_xcr0_get();

    // Field accessors
    pal_xcr0_sse_enable();
    pal_xcr0_sse_enable_from_value(value);
    pal_xcr0_sse_disable();
    pal_xcr0_sse_disable_from_value(value);
    pal_xcr0_sse_is_enabled();
    pal_xcr0_sse_is_enabled_from_value(value);
    pal_xcr0_sse_is_disabled();
    pal_xcr0_sse_is_disabled_from_value(value);

    // Printers
    pal_xcr0_dump();
    pal_xcr0_dump_from_value(value);
    pal_xcr0_sse_dump();
    pal_xcr0_sse_dump_from_value(value);
}
