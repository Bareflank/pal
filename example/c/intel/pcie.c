#include <stdlib.h>
#include <stdio.h>

#include "pal/pcie/config_space/header_type_0/vendor_id.h"
#include "pal/pcie/config_space/header_type_0/device_id.h"
#include "pal/pcie/config_space/header_type_0/status.h"
#include "pal/pcie/config_space/header_type_0/command.h"
#include "pal/pcie/config_space/header_type_0/bar.h"

void main(void)
{
    // Interact with PCI configuration space through PAL using the device's
    // bus/device/function address, and a "view" made from that address.
    // For example, here's how to set up PAL to observe a PCIe device located
    // at bus 2, device 0, function 0, with a "type 0" header.
    uint8_t bus = 0x2;
    uint8_t device = 0x0;
    uint8_t function = 0x0;
    uint32_t device_address = (1 << 31) | (bus << 24) | (device << 16) | (function << 8);
    pal_pcie_config_space_header_type_0_view view = {device_address};

    // Use the view to read a register from PCI configuration space like this:
    uint16_t vid = pal_get_pcie_config_space_header_type_0_vendor_id(&view);

    // Use the view to read and then pretty-print a list of registers from PCI
    // configuration space like this:
    pal_print_pcie_config_space_header_type_0_vendor_id(printf, &view);
    pal_print_pcie_config_space_header_type_0_device_id(printf, &view);
    pal_print_pcie_config_space_header_type_0_status(printf, &view);
    pal_print_pcie_config_space_header_type_0_command(printf, &view);

    // Base Address Registers (BARs) are accessed with an index 0 - 5 for
    // devices with a "type 0" header. You could walk through the device's BARs
    // to check their type (memory-mapped vs. I/O mapped) like this:
    uint32_t bar_value = 0;
    uint32_t bar_original_value = 0;
    for(int i = 0; i < 6; i++) {
        bar_original_value = pal_get_pcie_config_space_header_type_0_bar_at_index(&view, i);
        pal_set_pcie_config_space_header_type_0_bar_at_index(&view, 0xFFFFFFFF, i);
        bar_value = pal_get_pcie_config_space_header_type_0_bar_at_index(&view, i);
        if(pal_pcie_config_space_header_type_0_bar_memory_memory_space_indicator_is_enabled_in_value(bar_value)) {
            printf("BAR%u is type I/O\n", i);
        } else {
            printf("BAR%u is type memory\n", i);
        }
        pal_set_pcie_config_space_header_type_0_bar_at_index(&view, bar_original_value, i);
    }

}
