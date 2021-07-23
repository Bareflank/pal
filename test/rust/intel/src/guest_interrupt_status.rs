use pal;

pub fn test_guest_interrupt_status_compile()
{
    // Register accessors
    pal::vmcs::guest_interrupt_status::set(0xA55A);
    let mut value = pal::vmcs::guest_interrupt_status::get();

    // Field accessors
    pal::vmcs::guest_interrupt_status::get_rvi();
    pal::vmcs::guest_interrupt_status::get_rvi_from_value(value);
    pal::vmcs::guest_interrupt_status::set_rvi(0x0);
    pal::vmcs::guest_interrupt_status::set_rvi_in_value(0x0, &mut value);

    // Printers
    pal::vmcs::guest_interrupt_status::print();
    pal::vmcs::guest_interrupt_status::print_from_value(value);
    pal::vmcs::guest_interrupt_status::print_rvi();
    pal::vmcs::guest_interrupt_status::print_rvi_from_value(value);
}
