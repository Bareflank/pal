use pal;

pub unsafe fn test_leaf_0d_compile()
{
    let eax = pal::cpuid::leaf_0d_eax::get_at_index(1);
    let _ebx = pal::cpuid::leaf_0d_ebx::get_at_index(1);
    let _ecx = pal::cpuid::leaf_0d_ecx::get_at_index(1);
    let _edx = pal::cpuid::leaf_0d_edx::get_at_index(1);

    pal::cpuid::leaf_0d_eax::subleaf_0_sse_state_is_enabled_at_index(1);
    pal::cpuid::leaf_0d_eax::subleaf_0_sse_state_is_enabled_in_value(eax);
    pal::cpuid::leaf_0d_eax::subleaf_0_sse_state_is_disabled_at_index(1);
    pal::cpuid::leaf_0d_eax::subleaf_0_sse_state_is_disabled_in_value(eax);
    pal::cpuid::leaf_0d_eax::get_subleaf_0_mpx_state_at_index(1);
    pal::cpuid::leaf_0d_eax::get_subleaf_0_mpx_state_from_value(eax);

    #[cfg(feature = "pal/enable_printers")]
    {
    pal::cpuid::leaf_0d_eax::print_subleaf_0_at_index(1);
    pal::cpuid::leaf_0d_eax::print_subleaf_0_from_value(eax);
    pal::cpuid::leaf_0d_eax::print_subleaf_0_sse_state_at_index(1);
    pal::cpuid::leaf_0d_eax::print_subleaf_0_sse_state_from_value(eax);
    pal::cpuid::leaf_0d_eax::print_subleaf_0_mpx_state_at_index(1);
    pal::cpuid::leaf_0d_eax::print_subleaf_0_mpx_state_from_value(eax);
    }
}
