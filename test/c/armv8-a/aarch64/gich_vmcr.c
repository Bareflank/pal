#include <pal/external/gich_vmcr.h>

uintptr_t pal_gic_virtual_interface_control_base_address(void)
{ return 0; }

void test_gich_vmcr_compile(void)
{
    // Register accessors
    pal_gich_vmcr_set(0xA55A5AA5);
    uint64_t value = pal_gich_vmcr_get();

    // Field accessors
    pal_gich_vmcr_veng1_enable();
    pal_gich_vmcr_veng1_enable_from_value(value);
    pal_gich_vmcr_veng1_disable();
    pal_gich_vmcr_veng1_disable_from_value(value);
    pal_gich_vmcr_veng1_is_enabled();
    pal_gich_vmcr_veng1_is_enabled_from_value(value);
    pal_gich_vmcr_veng1_is_disabled();
    pal_gich_vmcr_veng1_is_disabled_from_value(value);
    pal_gich_vmcr_vbpr1_get();
    pal_gich_vmcr_vbpr1_get_from_value(value);
    pal_gich_vmcr_vbpr1_set(0x0);
    pal_gich_vmcr_vbpr1_set_from_value(0x0, value);

    // Printers
    pal_gich_vmcr_dump();
    pal_gich_vmcr_dump_from_value(value);
    pal_gich_vmcr_veng1_dump();
    pal_gich_vmcr_veng1_dump_from_value(value);
    pal_gich_vmcr_vbpr1_dump();
    pal_gich_vmcr_vbpr1_dump_from_value(value);
}
