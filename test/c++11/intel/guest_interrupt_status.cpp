#include <pal/vmcs/guest_interrupt_status.h>
#include <stdio.h>

void test_guest_interrupt_status_compile(void)
{
    // Register accessors
    pal::guest_interrupt_status::set(0xA55A);
    auto value = pal::guest_interrupt_status::get();

    // Field accessors
    pal::guest_interrupt_status::rvi::get();
    pal::guest_interrupt_status::rvi::get(value);
    pal::guest_interrupt_status::rvi::set(0x0);
    pal::guest_interrupt_status::rvi::set(0x0, value);

    // Printers
    pal::guest_interrupt_status::print(printf);
    pal::guest_interrupt_status::print(printf, value);
    pal::guest_interrupt_status::rvi::print(printf);
    pal::guest_interrupt_status::rvi::print(printf, value);
}
