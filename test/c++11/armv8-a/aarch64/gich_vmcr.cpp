#include <pal/external/gich_vmcr.h>

namespace pal
{
    uintptr_t gic_virtual_interface_control_base_address(void)
    { return 0; }
}

void test_gich_vmcr_compile(void)
{
    // Register accessors
    pal::gich_vmcr::set(0xA55A5AA5);
    auto value = pal::gich_vmcr::get();

    // Field accessors
    pal::gich_vmcr::veng1::enable();
    pal::gich_vmcr::veng1::enable(value);
    pal::gich_vmcr::veng1::disable();
    pal::gich_vmcr::veng1::disable(value);
    pal::gich_vmcr::veng1::is_enabled();
    pal::gich_vmcr::veng1::is_enabled(value);
    pal::gich_vmcr::veng1::is_disabled();
    pal::gich_vmcr::veng1::is_disabled(value);
    pal::gich_vmcr::vbpr1::get();
    pal::gich_vmcr::vbpr1::get(value);
    pal::gich_vmcr::vbpr1::set(0x0);
    pal::gich_vmcr::vbpr1::set(0x0, value);

    // Printers
    pal::gich_vmcr::print();
    pal::gich_vmcr::print(value);
    pal::gich_vmcr::veng1::print();
    pal::gich_vmcr::veng1::print(value);
    pal::gich_vmcr::vbpr1::print();
    pal::gich_vmcr::vbpr1::print(value);
}
