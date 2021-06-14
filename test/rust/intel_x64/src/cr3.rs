use pal;

pub fn test_cr3_compile()
{
    // Register accessors
    pal::control_register::cr3::set(0xA55A5AA5);
    let mut value = pal::control_register::cr3::get();

    // Field accessors
    pal::control_register::cr3::enable_pcd();
    pal::control_register::cr3::enable_pcd_in_value(&mut value);
    pal::control_register::cr3::disable_pcd();
    pal::control_register::cr3::disable_pcd_in_value(&mut value);
    pal::control_register::cr3::pcd_is_enabled();
    pal::control_register::cr3::pcd_is_enabled_in_value(value);
    pal::control_register::cr3::pcd_is_disabled();
    pal::control_register::cr3::pcd_is_disabled_in_value(value);
    pal::control_register::cr3::get_page_directory_base();
    pal::control_register::cr3::get_page_directory_base_from_value(value);
    pal::control_register::cr3::set_page_directory_base(0x0);
    pal::control_register::cr3::set_page_directory_base_in_value(0x0, &mut value);

    // Printers
    pal::control_register::cr3::print();
    pal::control_register::cr3::print_from_value(value);
    pal::control_register::cr3::print_pcd();
    pal::control_register::cr3::print_pcd_from_value(value);
    pal::control_register::cr3::print_page_directory_base();
    pal::control_register::cr3::print_page_directory_base_from_value(value);
}
