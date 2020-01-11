#include <pal/msr/ia32_feature_control.h>

void test_ia32_feature_control_compile(void)
{
    // Register accessors
    pal_ia32_feature_control_set(0xA55A5AA5);
    uint64_t value = pal_ia32_feature_control_get();

    // Field accessors
    pal_ia32_feature_control_enable_vmx_inside_smx_enable();
    pal_ia32_feature_control_enable_vmx_inside_smx_enable_from_value(value);
    pal_ia32_feature_control_enable_vmx_inside_smx_disable();
    pal_ia32_feature_control_enable_vmx_inside_smx_disable_from_value(value);
    pal_ia32_feature_control_enable_vmx_inside_smx_is_enabled();
    pal_ia32_feature_control_enable_vmx_inside_smx_is_enabled_from_value(value);
    pal_ia32_feature_control_enable_vmx_inside_smx_is_disabled();
    pal_ia32_feature_control_enable_vmx_inside_smx_is_disabled_from_value(value);
    pal_ia32_feature_control_senter_local_function_enable_get();
    pal_ia32_feature_control_senter_local_function_enable_get_from_value(value);
    pal_ia32_feature_control_senter_local_function_enable_set(0x0);
    pal_ia32_feature_control_senter_local_function_enable_set_from_value(0x0, value);

    // Printers
    pal_ia32_feature_control_dump();
    pal_ia32_feature_control_dump_from_value(value);
    pal_ia32_feature_control_enable_vmx_inside_smx_dump();
    pal_ia32_feature_control_enable_vmx_inside_smx_dump_from_value(value);
    pal_ia32_feature_control_senter_local_function_enable_dump();
    pal_ia32_feature_control_senter_local_function_enable_dump_from_value(value);
}
