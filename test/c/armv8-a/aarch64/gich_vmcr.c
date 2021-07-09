#include <pal/external/gich_vmcr.h>
#include <stdio.h>

uintptr_t pal_gic_virtual_interface_control_base_address(void)
{ return 0; }

void test_gich_vmcr_compile(void)
{
    // Register accessors
    pal_set_gich_vmcr(0xA55A5AA5);
    uint64_t value = pal_get_gich_vmcr();

    // Field accessors
    pal_enable_gich_vmcr_veng1();
    pal_enable_gich_vmcr_veng1_in_value(value);
    pal_disable_gich_vmcr_veng1();
    pal_disable_gich_vmcr_veng1_in_value(value);
    pal_gich_vmcr_veng1_is_enabled();
    pal_gich_vmcr_veng1_is_enabled_in_value(value);
    pal_gich_vmcr_veng1_is_disabled();
    pal_gich_vmcr_veng1_is_disabled_in_value(value);
    pal_get_gich_vmcr_vbpr1();
    pal_get_gich_vmcr_vbpr1_from_value(value);
    pal_set_gich_vmcr_vbpr1(0x0);
    pal_set_gich_vmcr_vbpr1_in_value(0x0, value);

    // Printers
    pal_print_gich_vmcr(printf);
    pal_print_gich_vmcr_from_value(printf, value);
    pal_print_gich_vmcr_veng1(printf);
    pal_print_gich_vmcr_veng1_from_value(printf, value);
    pal_print_gich_vmcr_vbpr1(printf);
    pal_print_gich_vmcr_vbpr1_from_value(printf, value);
}
