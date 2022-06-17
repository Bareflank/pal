use pal;

pub fn run_example() {
    // PAL lets you interact with instructions and registers using their name
    // as defined by a reference manual. For example, read the
    // SCTLR_EL1 system register, and then print its value:
    let sctlr_el1_value = pal::aarch64::sctlr_el1::get();
    pal::aarch64::sctlr_el1::print_from_value(sctlr_el1_value);

    // Registers that contain named fields can also be accessed by name.
    // For example, check if EL0 execution of cache maintenance instructions are 
    // trapped to EL1 by reading the UCI field (bit 26) in SCTLR_EL1
    if pal::aarch64::sctlr_el1::uci_is_enabled() {
        println!("EL0 execution of cache maintenance instructions are trapped to EL1!");
    }
}
