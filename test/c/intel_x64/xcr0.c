#include <pal/control_register/xcr0.h>

void test_xcr0_compile(void)
{
    // Register accessors
    pal_set_xcr0(0xA55A5AA5);
    uint64_t value = pal_get_xcr0();

    // Field accessors
    pal_enable_xcr0_sse();
    pal_enable_xcr0_sse_in_value(value);
    pal_disable_xcr0_sse();
    pal_disable_xcr0_sse_in_value(value);
    pal_xcr0_sse_is_enabled();
    pal_xcr0_sse_is_enabled_in_value(value);
    pal_xcr0_sse_is_disabled();
    pal_xcr0_sse_is_disabled_in_value(value);

    // Printers
    pal_print_xcr0();
    pal_print_xcr0_from_value(value);
    pal_print_xcr0_sse();
    pal_print_xcr0_sse_from_value(value);
}
