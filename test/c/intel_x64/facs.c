#include <pal/acpi/facs/flags.h>
#include <pal/acpi/facs/version.h>
#include <stdio.h>

void test_facs_compile(void)
{
    const pal_acpi_facs_table_view view = {0xF00DBEEF};

    // Register accessors
    pal_set_acpi_facs_table_version(&view, 0xA55A5AA5);
    uint32_t value = pal_get_acpi_facs_table_version(&view);
    uint32_t value2 = pal_get_acpi_facs_table_flags(&view);

    // Field accessors
    pal_enable_acpi_facs_table_flags_s4bios_f(&view);
    pal_enable_acpi_facs_table_flags_s4bios_f_in_value(value);
    pal_disable_acpi_facs_table_flags_s4bios_f(&view);
    pal_disable_acpi_facs_table_flags_s4bios_f_in_value(value);
    pal_acpi_facs_table_flags_s4bios_f_is_enabled(&view);
    pal_acpi_facs_table_flags_s4bios_f_is_enabled_in_value(value);
    pal_acpi_facs_table_flags_s4bios_f_is_disabled(&view);
    pal_acpi_facs_table_flags_s4bios_f_is_disabled_in_value(value);
    pal_get_acpi_facs_table_version_version(&view);
    pal_get_acpi_facs_table_version_version_from_value(value);
    pal_set_acpi_facs_table_version_version(&view, 0x0);
    pal_set_acpi_facs_table_version_version_in_value(0x0, value);

    // Printers
    pal_print_acpi_facs_table_version(printf, &view);
    pal_print_acpi_facs_table_version_from_value(printf, value);
    pal_print_acpi_facs_table_flags_s4bios_f(printf, &view);
    pal_print_acpi_facs_table_flags_s4bios_f_from_value(printf, value);
    pal_print_acpi_facs_table_version_version(printf, &view);
    pal_print_acpi_facs_table_version_version_from_value(printf, value);
}
