#include <pal/msr/ia32_feature_control.h>

void test_ia32_feature_control_compile(void)
{
    // Register accessors
    pal::ia32_feature_control::set(0xA55A5AA5);
    auto value = pal::ia32_feature_control::get();

    // Field accessors
    pal::ia32_feature_control::enable_vmx_inside_smx::enable();
    pal::ia32_feature_control::enable_vmx_inside_smx::enable(value);
    pal::ia32_feature_control::enable_vmx_inside_smx::disable();
    pal::ia32_feature_control::enable_vmx_inside_smx::disable(value);
    pal::ia32_feature_control::enable_vmx_inside_smx::is_enabled();
    pal::ia32_feature_control::enable_vmx_inside_smx::is_enabled(value);
    pal::ia32_feature_control::enable_vmx_inside_smx::is_disabled();
    pal::ia32_feature_control::enable_vmx_inside_smx::is_disabled(value);
    pal::ia32_feature_control::senter_local_function_enable::get();
    pal::ia32_feature_control::senter_local_function_enable::get(value);
    pal::ia32_feature_control::senter_local_function_enable::set(0x0);
    pal::ia32_feature_control::senter_local_function_enable::set(0x0, value);

    // Printers
    pal::ia32_feature_control::print();
    pal::ia32_feature_control::print(value);
    pal::ia32_feature_control::enable_vmx_inside_smx::print();
    pal::ia32_feature_control::enable_vmx_inside_smx::print(value);
    pal::ia32_feature_control::senter_local_function_enable::print();
    pal::ia32_feature_control::senter_local_function_enable::print(value);
}
