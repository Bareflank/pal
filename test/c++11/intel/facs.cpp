#include <pal/acpi/facs/flags.h>
#include <pal/acpi/facs/version.h>
#include <pal/instruction/read_mem.h>
#include <pal/instruction/write_mem.h>
#include <stdio.h>

void test_facs_compile(void)
{
    void * address = 0xF00DBEEF;
    auto read_fn = pal::execute_read_mem;
    auto write_fn = pal::execute_write_mem;
    auto facs_view = pal::make_acpi_facs_view(address, read_fn, write_fn);

    // Register accessors
    pal::acpi::facs::version::set(0xA55A5AA5);
    auto value = pal::acpi::facs::flags::get();

    // Field accessors
    pal::acpi::facs::flags::s4bios_f::enable();
    pal::acpi::facs::flags::s4bios_f::enable(value);
    pal::acpi::facs::flags::s4bios_f::disable();
    pal::acpi::facs::flags::s4bios_f::disable(value);
    pal::acpi::facs::flags::s4bios_f::is_enabled();
    pal::acpi::facs::flags::s4bios_f::is_enabled(value);
    pal::acpi::facs::flags::s4bios_f::is_disabled();
    pal::acpi::facs::flags::s4bios_f::is_disabled(value);
    pal::acpi::facs::version::version::get();
    pal::acpi::facs::version::version::get(value);
    pal::acpi::facs::version::version::set(0x0);
    pal::acpi::facs::version::version::set(0x0, value);

    // Printers
    pal::acpi::facs::version::print(printf);
    pal::acpi::facs::version::print(printf, value);
    pal::acpi::facs::flags::s4bios_f::print(printf);
    pal::acpi::facs::flags::s4bios_f::print(printf, value);
    pal::acpi::facs::version::version::print(printf);
    pal::acpi::facs::version::version::print(printf, value);
}
