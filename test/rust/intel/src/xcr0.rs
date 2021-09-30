use pal;

pub unsafe fn test_xcr0_compile()
{
    // Register accessors
    pal::control_register::xcr0::set(0xA55A5AA5);
    let mut value = pal::control_register::xcr0::get();

    // Field accessors
    pal::control_register::xcr0::enable_sse();
    pal::control_register::xcr0::enable_sse_in_value(&mut value);
    pal::control_register::xcr0::disable_sse();
    pal::control_register::xcr0::disable_sse_in_value(&mut value);
    pal::control_register::xcr0::sse_is_enabled();
    pal::control_register::xcr0::sse_is_enabled_in_value(value);
    pal::control_register::xcr0::sse_is_disabled();
    pal::control_register::xcr0::sse_is_disabled_in_value(value);

    #[cfg(feature = "pal/enable_printers")]
    {
    // Printers
    pal::control_register::xcr0::print();
    pal::control_register::xcr0::print_from_value(value);
    pal::control_register::xcr0::print_sse();
    pal::control_register::xcr0::print_sse_from_value(value);
    }
}
