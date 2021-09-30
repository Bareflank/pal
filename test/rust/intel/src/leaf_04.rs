use pal;

pub unsafe fn test_leaf_04_compile()
{
    let eax = pal::cpuid::leaf_04_eax::get_at_index(1);
    let _ebx = pal::cpuid::leaf_04_ebx::get_at_index(1);
    let _ecx = pal::cpuid::leaf_04_ecx::get_at_index(1);
    let _edx = pal::cpuid::leaf_04_edx::get_at_index(1);

    pal::cpuid::leaf_04_eax::self_initializing_cache_level_is_enabled_at_index(1);
    pal::cpuid::leaf_04_eax::self_initializing_cache_level_is_enabled_in_value(eax);
    pal::cpuid::leaf_04_eax::self_initializing_cache_level_is_disabled_at_index(1);
    pal::cpuid::leaf_04_eax::self_initializing_cache_level_is_disabled_in_value(eax);
    pal::cpuid::leaf_04_eax::get_cache_type_at_index(1);
    pal::cpuid::leaf_04_eax::get_cache_type_from_value(eax);

    #[cfg(feature = "pal/enable_printers")]
    {
    pal::cpuid::leaf_04_eax::print_at_index(1);
    pal::cpuid::leaf_04_eax::print_from_value(eax);
    pal::cpuid::leaf_04_eax::print_self_initializing_cache_level_at_index(1);
    pal::cpuid::leaf_04_eax::print_self_initializing_cache_level_from_value(eax);
    pal::cpuid::leaf_04_eax::print_cache_type_at_index(1);
    pal::cpuid::leaf_04_eax::print_cache_type_from_value(eax);
    }
}
