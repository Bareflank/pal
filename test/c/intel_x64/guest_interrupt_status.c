#include <pal/vmcs/guest_interrupt_status.h>

void test_guest_interrupt_status_compile(void)
{
    // Register accessors
    pal_guest_interrupt_status_set(0xA55A);
    uint16_t value = pal_guest_interrupt_status_get();

    // Field accessors
    pal_guest_interrupt_status_rvi_get();
    pal_guest_interrupt_status_rvi_get_from_value(value);
    pal_guest_interrupt_status_rvi_set(0x0);
    pal_guest_interrupt_status_rvi_set_from_value(0x0, value);

    // Printers
    pal_guest_interrupt_status_dump();
    pal_guest_interrupt_status_dump_from_value(value);
    pal_guest_interrupt_status_rvi_dump();
    pal_guest_interrupt_status_rvi_dump_from_value(value);
}
