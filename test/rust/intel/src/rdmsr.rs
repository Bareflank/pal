use pal;

pub unsafe fn test_rdmsr_compile()
{
    let address = pal::msr::ia32_feature_control::ADDRESS;
    let value = pal::instruction::execute_rdmsr(address);

    #[cfg(feature = "pal/enable_printers")]
    pal::msr::ia32_feature_control::print_from_value(value);

    #[cfg(not(feature = "pal/enable_printers"))]
    let _ = value;
}
