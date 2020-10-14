#include <pal/acpi/facs_flags.h>
#include <pal/acpi/facs_version.h>

namespace pal
{
    uintptr_t facs_base_address(void)
    { return 0; }
}

void test_facs_compile(void)
{
    // Register accessors
    pal::facs_version::set(0xA55A5AA5);
    auto value = pal::facs_flags::get();

    // Field accessors
    pal::facs_flags::s4bios_f::enable();
    pal::facs_flags::s4bios_f::enable(value);
    pal::facs_flags::s4bios_f::disable();
    pal::facs_flags::s4bios_f::disable(value);
    pal::facs_flags::s4bios_f::is_enabled();
    pal::facs_flags::s4bios_f::is_enabled(value);
    pal::facs_flags::s4bios_f::is_disabled();
    pal::facs_flags::s4bios_f::is_disabled(value);
    pal::facs_version::version::get();
    pal::facs_version::version::get(value);
    pal::facs_version::version::set(0x0);
    pal::facs_version::version::set(0x0, value);

    // Printers
    pal::facs_version::print();
    pal::facs_version::print(value);
    pal::facs_flags::s4bios_f::print();
    pal::facs_flags::s4bios_f::print(value);
    pal::facs_version::version::print();
    pal::facs_version::version::print(value);
}
