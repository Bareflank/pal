use pal;

pub fn test_rdmsr_compile()
{
    let address = pal::msr::ia32_feature_control::ADDRESS;
    let value = pal::instruction::execute_rdmsr(address);
    pal::msr::ia32_feature_control::print_from_value(value);
}
