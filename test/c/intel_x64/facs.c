#include <pal/acpi/facs_flags.h>
#include <pal/acpi/facs_version.h>

uintptr_t pal_facs_base_address(void)
{ return 0; }

void test_facs_compile(void)
{
    // Register accessors
    pal_facs_version_set(0xA55A5AA5);
    uint32_t value = pal_facs_flags_get();

    // Field accessors
    pal_facs_flags_s4bios_f_enable();
    pal_facs_flags_s4bios_f_enable_from_value(value);
    pal_facs_flags_s4bios_f_disable();
    pal_facs_flags_s4bios_f_disable_from_value(value);
    pal_facs_flags_s4bios_f_is_enabled();
    pal_facs_flags_s4bios_f_is_enabled_from_value(value);
    pal_facs_flags_s4bios_f_is_disabled();
    pal_facs_flags_s4bios_f_is_disabled_from_value(value);
    pal_facs_version_version_get();
    pal_facs_version_version_get_from_value(value);
    pal_facs_version_version_set(0x0);
    pal_facs_version_version_set_from_value(0x0, value);

    // Printers
    pal_facs_version_print();
    pal_facs_version_print_from_value(value);
    pal_facs_flags_s4bios_f_print();
    pal_facs_flags_s4bios_f_print_from_value(value);
    pal_facs_version_version_print();
    pal_facs_version_version_print_from_value(value);
}

