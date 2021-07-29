#include "pal/pcie/config_space/header_type_0/vendor_id.h"
#include "pal/pcie/config_space/header_type_0/device_id.h"
#include "pal/pcie/config_space/header_type_0/command.h"
#include "pal/pcie/config_space/header_type_0/bar.h"
#include <stdio.h>

void test_pcie_compile(void)
{
    namespace pci_header = pal::pcie_config_space_header_type_0;
    const auto view = pci_header::view{0xf00dbeef};

    // Register accessors
    uint16_t vid = pci_header::vendor_id::get(view);
    uint16_t did = pci_header::device_id::get(view);
    uint16_t command = pci_header::command::get(view);
    pci_header::vendor_id::set(view, 0xFFFF);
    pci_header::device_id::set(view, 0xFFFF);
    pci_header::command::set(view, 0xFFFF);

    // Indexed register accessors
    uint32_t bar0 = pci_header::bar::get_at_index(view, 0);
    uint32_t bar1 = pci_header::bar::get_at_index(view, 1);
    pci_header::bar::set_at_index(view, 0xFFFFFFFF, 0);
    pci_header::bar::set_at_index(view, 0xFFFFFFFF, 1);

    // Field accessors
    pci_header::command::memory_space_enable::enable(view);
    pci_header::command::memory_space_enable::enable(command);
    pci_header::command::memory_space_enable::disable(view);
    pci_header::command::memory_space_enable::disable(command);
    pci_header::command::memory_space_enable::is_enabled(view);
    pci_header::command::memory_space_enable::is_enabled(command);
    pci_header::command::memory_space_enable::is_disabled(view);
    pci_header::command::memory_space_enable::is_disabled(command);
    pci_header::bar::memory::base_address::get_at_index(view, 0);
    pci_header::bar::memory::base_address::get(bar0);
    pci_header::bar::memory::base_address::set_at_index(view, 0x0, 0);
    pci_header::bar::memory::base_address::set(0x0, bar0);

    // Printers
    pci_header::command::memory_space_enable::print(printf, view);
    pci_header::command::memory_space_enable::print(printf, command);
    pci_header::bar::memory::base_address::print_at_index(printf, view, 0);
    pci_header::bar::memory::base_address::print(printf, bar0);
}
