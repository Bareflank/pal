#include <pal/msr/ia32_feature_control.h>

void test_ia32_feature_control_compile(void)
{
    // Register accessors
    pal_set_ia32_feature_control(0xA55A5AA5);
    uint64_t value = pal_get_ia32_feature_control();

    // Field accessors
    pal_enable_ia32_feature_control_enable_vmx_inside_smx();
    pal_enable_ia32_feature_control_enable_vmx_inside_smx_in_value(value);
    pal_disable_ia32_feature_control_enable_vmx_inside_smx();
    pal_disable_ia32_feature_control_enable_vmx_inside_smx_in_value(value);
    pal_ia32_feature_control_enable_vmx_inside_smx_is_enabled();
    pal_ia32_feature_control_enable_vmx_inside_smx_is_enabled_in_value(value);
    pal_ia32_feature_control_enable_vmx_inside_smx_is_disabled();
    pal_ia32_feature_control_enable_vmx_inside_smx_is_disabled_in_value(value);
    pal_get_ia32_feature_control_senter_local_function_enable();
    pal_get_ia32_feature_control_senter_local_function_enable_from_value(value);
    pal_set_ia32_feature_control_senter_local_function_enable(0x0);
    pal_set_ia32_feature_control_senter_local_function_enable_in_value(0x0, value);

    // Printers
    pal_print_ia32_feature_control();
    pal_print_ia32_feature_control_from_value(value);
    pal_print_ia32_feature_control_enable_vmx_inside_smx();
    pal_print_ia32_feature_control_enable_vmx_inside_smx_from_value(value);
    pal_print_ia32_feature_control_senter_local_function_enable();
    pal_print_ia32_feature_control_senter_local_function_enable_from_value(value);
}
