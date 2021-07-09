#include <pal/vmcs/guest_interrupt_status.h>
#include <stdio.h>

void test_guest_interrupt_status_compile(void)
{
    // Register accessors
    pal_set_guest_interrupt_status(0xA55A);
    uint16_t value = pal_get_guest_interrupt_status();

    // Field accessors
    pal_get_guest_interrupt_status_rvi();
    pal_get_guest_interrupt_status_rvi_from_value(value);
    pal_set_guest_interrupt_status_rvi(0x0);
    pal_set_guest_interrupt_status_rvi_in_value(0x0, value);

    // Printers
    pal_print_guest_interrupt_status(printf);
    pal_print_guest_interrupt_status_from_value(printf, value);
    pal_print_guest_interrupt_status_rvi(printf);
    pal_print_guest_interrupt_status_rvi_from_value(printf, value);
}
