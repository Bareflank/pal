use pal;

pub fn test_leaf_01_compile()
{
    let eax = pal::cpuid::leaf_01_eax::get();
    let _ebx = pal::cpuid::leaf_01_ebx::get();
    let _ecx = pal::cpuid::leaf_01_ecx::get();
    let _edx = pal::cpuid::leaf_01_edx::get();

    let _value = pal::cpuid::leaf_01_eax::get_model();
    let _value2 = pal::cpuid::leaf_01_eax::get_model_from_value(eax);

    pal::cpuid::leaf_01_eax::print();
    pal::cpuid::leaf_01_eax::print_from_value(eax);
    pal::cpuid::leaf_01_eax::print_model();
    pal::cpuid::leaf_01_eax::print_model_from_value(eax);
}
