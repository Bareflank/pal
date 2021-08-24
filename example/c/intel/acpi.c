#include <stdlib.h>
#include <stdio.h>
#include "pal/acpi/facs/firmware_waking_vector.h"
#include "pal/acpi/facs/flags.h"
#include "pal/acpi/facs/global_lock.h"
#include "pal/acpi/facs/hardware_signature.h"
#include "pal/acpi/facs/length.h"
#include "pal/acpi/facs/ospm_flags.h"
#include "pal/acpi/facs/signature.h"
#include "pal/acpi/facs/version.h"
#include "pal/acpi/facs/x_firmware_waking_vector.h"

void main(void)
{
    // To interact with memory-mapped resources with PAL (e.g. ACPI FACS table),
    // it's your job to first map the resource as memory into your program
    // (process, driver, firmware, etc). For this example, we'll allocate an
    // empty buffer and "interpret it" as the ACPI FACS table:
    void * buffer = malloc(1024);
    if(!buffer) {
        printf("Malloc failed!\n");
        return;
    }

    // Next, use the pointer that maps your resource to create a "view":
    pal_acpi_facs_table_view facs_view = {(uintptr_t)buffer};

    // Use the view to read and write the registers and fields of the memory
    // mapped resource. For example, read and write the "flags" register in the
    // FACS table:
    uint32_t flags = pal_get_acpi_facs_table_flags(&facs_view);
    pal_set_acpi_facs_table_flags(&facs_view, 0xf00dbeef);

    // You could enable the individual "s4bios_f" bitfield from the flags
    // register like this:
    pal_enable_acpi_facs_table_flags_s4bios_f(&facs_view);

    // Or check that the "s4bios_f" bitfield is enabled like this:
    pal_acpi_facs_table_flags_s4bios_f_is_enabled(&facs_view);

    // Or use the view to read and pretty-print a list of registers from the
    // FACS table like this:
    pal_print_acpi_facs_table_firmware_waking_vector(printf, &facs_view);
    pal_print_acpi_facs_table_flags(printf, &facs_view);
    pal_print_acpi_facs_table_global_lock(printf, &facs_view);
    pal_print_acpi_facs_table_hardware_signature(printf, &facs_view);
    pal_print_acpi_facs_table_length(printf, &facs_view);
    pal_print_acpi_facs_table_ospm_flags(printf, &facs_view);
    pal_print_acpi_facs_table_signature(printf, &facs_view);
    pal_print_acpi_facs_table_version(printf, &facs_view);
    pal_print_acpi_facs_table_x_firmware_waking_vector(printf, &facs_view);
}
