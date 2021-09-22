use pal;

pub fn test_read_cr3_compile()
{
    let value = pal::instruction::execute_read_cr3();

    #[cfg(feature = "pal/enable_printers")]
    pal::control_register::cr3::print_from_value(value);

    #[cfg(not(feature = "pal/enable_printers"))]
    let _ = value;
}
