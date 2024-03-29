#include <pal/cpuid/leaf_0d_eax.h>
#include <pal/cpuid/leaf_0d_ebx.h>
#include <pal/cpuid/leaf_0d_ecx.h>
#include <pal/cpuid/leaf_0d_edx.h>
#include <stdio.h>

void test_leaf_0d_compile(void)
{
    // Register accessors
    auto eax = pal::leaf_0d_eax::get_at_index(1);
    auto ebx = pal::leaf_0d_ebx::get_at_index(1);
    auto ecx = pal::leaf_0d_ecx::get_at_index(1);
    auto edx = pal::leaf_0d_edx::get_at_index(1);

    // Field accessors
    pal::leaf_0d_eax::subleaf_0::sse_state::is_enabled_at_index(1);
    pal::leaf_0d_eax::subleaf_0::sse_state::is_enabled(eax);
    pal::leaf_0d_eax::subleaf_0::sse_state::is_disabled_at_index(1);
    pal::leaf_0d_eax::subleaf_0::sse_state::is_disabled(eax);
    pal::leaf_0d_eax::subleaf_0::mpx_state::get_at_index(1);
    pal::leaf_0d_eax::subleaf_0::mpx_state::get(eax);

    // Printers
    pal::leaf_0d_eax::subleaf_0::print_at_index(printf, 1);
    pal::leaf_0d_eax::subleaf_0::print(printf, eax);
    pal::leaf_0d_eax::subleaf_0::sse_state::print_at_index(printf, 1);
    pal::leaf_0d_eax::subleaf_0::sse_state::print(printf, eax);
    pal::leaf_0d_eax::subleaf_0::mpx_state::print_at_index(printf, 1);
    pal::leaf_0d_eax::subleaf_0::mpx_state::print(printf, eax);
}
