use pal;

pub fn test_eptp_compile()
{
    // Register accessors
    pal::vmcs::eptp::set(0xA55A5AA5);
    let mut value = pal::vmcs::eptp::get();

    // Field accessors
    pal::vmcs::eptp::enable_bit_6();
    pal::vmcs::eptp::enable_bit_6_in_value(&mut value);
    pal::vmcs::eptp::disable_bit_6();
    pal::vmcs::eptp::disable_bit_6_in_value(&mut value);
    pal::vmcs::eptp::bit_6_is_enabled();
    pal::vmcs::eptp::bit_6_is_enabled_in_value(value);
    pal::vmcs::eptp::bit_6_is_disabled();
    pal::vmcs::eptp::bit_6_is_disabled_in_value(value);
    pal::vmcs::eptp::get_ept_pml4_table();
    pal::vmcs::eptp::get_ept_pml4_table_from_value(value);
    pal::vmcs::eptp::set_ept_pml4_table(0x0);
    pal::vmcs::eptp::set_ept_pml4_table_in_value(0x0, &mut value);

    #[cfg(feature = "pal/enable_printers")]
    {
    // Printers
    pal::vmcs::eptp::print();
    pal::vmcs::eptp::print_from_value(value);
    pal::vmcs::eptp::print_bit_6();
    pal::vmcs::eptp::print_bit_6_from_value(value);
    pal::vmcs::eptp::print_ept_pml4_table();
    pal::vmcs::eptp::print_ept_pml4_table_from_value(value);
    }
}
