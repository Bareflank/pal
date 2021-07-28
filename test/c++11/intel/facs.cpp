#include <pal/acpi/facs/flags.h>
#include <pal/acpi/facs/version.h>
#include <stdio.h>

void test_facs_compile(void)
{
    namespace facs = pal::acpi_facs_table;
    const auto view = facs::view{0xf00dbeef};

    // Register accessors
    facs::version::set(view, 0xA55A5AA5);
    auto value = facs::flags::get(view);

    // Field accessors
    facs::flags::s4bios_f::enable(view);
    facs::flags::s4bios_f::enable(value);
    facs::flags::s4bios_f::disable(view);
    facs::flags::s4bios_f::disable(value);
    facs::flags::s4bios_f::is_enabled(view);
    facs::flags::s4bios_f::is_enabled(value);
    facs::flags::s4bios_f::is_disabled(view);
    facs::flags::s4bios_f::is_disabled(value);
    facs::version::version::get(view);
    facs::version::version::get(value);
    facs::version::version::set(view, 0x0);
    facs::version::version::set(0x0, value);

    // Printers
    facs::version::print(printf, view);
    facs::version::print(printf, value);
    facs::flags::s4bios_f::print(printf, view);
    facs::flags::s4bios_f::print(printf, value);
    facs::version::version::print(printf, view);
    facs::version::version::print(printf, value);
}
