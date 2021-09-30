use pal;

pub unsafe fn test_cpuid_compile()
{
    let leaf = 0x1;
    let subleaf = 0x0;

    let (eax, ebx, ecx, edx) = pal::instruction::execute_cpuid(leaf, subleaf);

    #[cfg(feature = "pal/enable_printers")]
    {
    pal::cpuid::leaf_01_eax::print_from_value(eax);
    pal::cpuid::leaf_01_ebx::print_from_value(ebx);
    pal::cpuid::leaf_01_ecx::print_from_value(ecx);
    pal::cpuid::leaf_01_edx::print_from_value(edx);
    }

    #[cfg(not(feature = "pal/enable_printers"))]
    let _ = (eax, ebx, ecx, edx);
}
