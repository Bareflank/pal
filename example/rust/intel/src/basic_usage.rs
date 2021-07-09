use pal;

pub fn run_example() {
    // PAL lets you interact with instructions and registers using their name
    // as defined by a reference manual. For example, read the
    // IA32_FEATURE_CONTROL MSR, and then print its value:
    let msr_value = pal::msr::ia32_feature_control::get();
    pal::msr::ia32_feature_control::print_from_value(msr_value);

    // As another example, read the IA32_TSC MSR using its address as an input
    // to the x86 RDMSR instruction
    let address = pal::msr::ia32_tsc::ADDRESS;
    let _msr_value_2 = pal::instruction::execute_rdmsr(address);

    // You can also print register contents without storing the value in a
    // variable. For example, print part of a CPUID leaf:
    pal::cpuid::leaf_01_eax::print();

    // In Rust, instructions that logically output more than one value are
    // returned by PAL as tuples for easy integration with std::tie:
    let (eax, ebx, ecx, edx) = pal::instruction::execute_cpuid(0x02, 0x00);
    pal::cpuid::leaf_02_eax::print_from_value(eax);
    pal::cpuid::leaf_02_ebx::print_from_value(ebx);
    pal::cpuid::leaf_02_ecx::print_from_value(ecx);
    pal::cpuid::leaf_02_edx::print_from_value(edx);

    // Registers that contain named fields can also be accessed by name.
    // For example, check if paging is enabled by reading the PG bit in control 
    // register CR0
    if pal::control_register::cr0::pg_is_enabled() {
        println!("Paging is enabled!");
    }
}
