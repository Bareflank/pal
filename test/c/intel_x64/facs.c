#include <pal/acpi/facs/flags.h>
#include <pal/acpi/facs/version.h>
#include <pal/instruction/read_mem.h>
#include <pal/instruction/write_mem.h>
#include <stdio.h>

void test_facs_compile(void)
{
    void * address = 0xF00DBEEF;
    pal_read_function read_fn = pal_execute_read_mem;
    pal_write_function write_fn = pal_execute_write_mem;
    pal_acpi_facs_view view = pal_make_acpi_facs_view(address, read_fn, write_fn);

    // Register accessors
    pal_set_facs_version(&view, 0xA55A5AA5);
    uint32_t value = pal_get_facs_version(&view);
    uint32_t value2 = pal_get_facs_flags(&view);

    // Field accessors
    pal_enable_facs_flags_s4bios_f(&view);
    pal_enable_facs_flags_s4bios_f_in_value(value);
    pal_disable_facs_flags_s4bios_f(&view);
    pal_disable_facs_flags_s4bios_f_in_value(value);
    pal_facs_flags_s4bios_f_is_enabled(&view);
    pal_facs_flags_s4bios_f_is_enabled_in_value(value);
    pal_facs_flags_s4bios_f_is_disabled(&view);
    pal_facs_flags_s4bios_f_is_disabled_in_value(value);
    pal_get_facs_version_version(&view);
    pal_get_facs_version_version_from_value(value);
    pal_set_facs_version_version(&view, 0x0);
    pal_set_facs_version_version_in_value(0x0, value);

    // Printers
    pal_print_facs_version(printf, &view);
    pal_print_facs_version_from_value(printf, value);
    pal_print_facs_flags_s4bios_f(printf, &view);
    pal_print_facs_flags_s4bios_f_from_value(printf, value);
    pal_print_facs_version_version(printf, &view);
    pal_print_facs_version_version_from_value(printf, value);
}
