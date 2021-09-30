use pal;

pub unsafe fn test_ia32_feature_control_compile()
{
    // Register accessors
    pal::msr::ia32_feature_control::set(0xA55A5AA5A55A5AA5);
    let mut value = pal::msr::ia32_feature_control::get();

    // Field accessors
    pal::msr::ia32_feature_control::enable_enable_vmx_inside_smx();
    pal::msr::ia32_feature_control::enable_enable_vmx_inside_smx_in_value(&mut value);
    pal::msr::ia32_feature_control::disable_enable_vmx_inside_smx();
    pal::msr::ia32_feature_control::disable_enable_vmx_inside_smx_in_value(&mut value);
    pal::msr::ia32_feature_control::enable_vmx_inside_smx_is_enabled();
    pal::msr::ia32_feature_control::enable_vmx_inside_smx_is_enabled_in_value(value);
    pal::msr::ia32_feature_control::enable_vmx_inside_smx_is_disabled();
    pal::msr::ia32_feature_control::enable_vmx_inside_smx_is_disabled_in_value(value);
    pal::msr::ia32_feature_control::get_senter_local_function_enable();
    pal::msr::ia32_feature_control::get_senter_local_function_enable_from_value(value);
    pal::msr::ia32_feature_control::set_senter_local_function_enable(0x0);
    pal::msr::ia32_feature_control::set_senter_local_function_enable_in_value(0x0, &mut value);

    #[cfg(feature = "pal/enable_printers")]
    {
    // Printers
    pal::msr::ia32_feature_control::print();
    pal::msr::ia32_feature_control::print_from_value(value);
    pal::msr::ia32_feature_control::print_enable_vmx_inside_smx();
    pal::msr::ia32_feature_control::print_enable_vmx_inside_smx_from_value(value);
    pal::msr::ia32_feature_control::print_senter_local_function_enable();
    pal::msr::ia32_feature_control::print_senter_local_function_enable_from_value(value);
    }
}
