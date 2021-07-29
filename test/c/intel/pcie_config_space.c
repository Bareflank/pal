#include "pal/pcie/config_space/header_type_0/vendor_id.h"
#include "pal/pcie/config_space/header_type_0/device_id.h"
#include "pal/pcie/config_space/header_type_0/command.h"
#include "pal/pcie/config_space/header_type_0/bar.h"
#include <stdio.h>

void test_pcie_compile(void)
{
    const pal_pcie_config_space_header_type_0_view view = {0xF00DBEEF};

    // Register accessors
    uint16_t vid = pal_get_pcie_config_space_header_type_0_vendor_id(&view);
    uint16_t did = pal_get_pcie_config_space_header_type_0_device_id(&view);
    uint16_t command = pal_get_pcie_config_space_header_type_0_command(&view);
    pal_set_pcie_config_space_header_type_0_vendor_id(&view, 0xFFFF);
    pal_set_pcie_config_space_header_type_0_device_id(&view, 0xFFFF);
    pal_set_pcie_config_space_header_type_0_command(&view, 0xFFFF);

    // Indexed register accessors
    uint32_t bar0 = pal_get_pcie_config_space_header_type_0_bar_at_index(&view, 0);
    uint32_t bar1 = pal_get_pcie_config_space_header_type_0_bar_at_index(&view, 1);
    pal_set_pcie_config_space_header_type_0_bar_at_index(&view, 0xFFFFFFFF, 0);
    pal_set_pcie_config_space_header_type_0_bar_at_index(&view, 0xFFFFFFFF, 1);

    // Field accessors
    pal_enable_pcie_config_space_header_type_0_command_memory_space_enable(&view);
    pal_enable_pcie_config_space_header_type_0_command_memory_space_enable_in_value(command);
    pal_disable_pcie_config_space_header_type_0_command_memory_space_enable(&view);
    pal_disable_pcie_config_space_header_type_0_command_memory_space_enable_in_value(command);
    pal_pcie_config_space_header_type_0_command_memory_space_enable_is_enabled(&view);
    pal_pcie_config_space_header_type_0_command_memory_space_enable_is_enabled_in_value(command);
    pal_pcie_config_space_header_type_0_command_memory_space_enable_is_disabled(&view);
    pal_pcie_config_space_header_type_0_command_memory_space_enable_is_disabled_in_value(command);
    pal_get_pcie_config_space_header_type_0_bar_memory_base_address_at_index(&view, 0);
    pal_get_pcie_config_space_header_type_0_bar_memory_base_address_from_value(bar0);
    pal_set_pcie_config_space_header_type_0_bar_memory_base_address_at_index(&view, 0x0, 0);
    pal_set_pcie_config_space_header_type_0_bar_memory_base_address_in_value(0x0, bar0);

    // Printers
    pal_print_pcie_config_space_header_type_0_command_memory_space_enable(printf, &view);
    pal_print_pcie_config_space_header_type_0_command_memory_space_enable_from_value(printf, command);
    pal_print_pcie_config_space_header_type_0_bar_memory_base_address_at_index(printf, &view, 0);
    pal_print_pcie_config_space_header_type_0_bar_memory_base_address_from_value(printf, bar0);
}
