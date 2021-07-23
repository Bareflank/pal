#include <pal/cpuid/leaf_0d_eax.h>
#include <pal/cpuid/leaf_0d_ebx.h>
#include <pal/cpuid/leaf_0d_ecx.h>
#include <pal/cpuid/leaf_0d_edx.h>
#include <stdio.h>

void test_leaf_0d_compile(void)
{
    // Register accessors
    uint32_t eax = pal_get_leaf_0d_eax_at_index(1);
    uint32_t ebx = pal_get_leaf_0d_ebx_at_index(1);
    uint32_t ecx = pal_get_leaf_0d_ecx_at_index(1);
    uint32_t edx = pal_get_leaf_0d_edx_at_index(1);

    // Field accessors
    pal_leaf_0d_eax_subleaf_0_sse_state_is_enabled_at_index(1);
    pal_leaf_0d_eax_subleaf_0_sse_state_is_enabled_in_value(eax);
    pal_leaf_0d_eax_subleaf_0_sse_state_is_disabled_at_index(1);
    pal_leaf_0d_eax_subleaf_0_sse_state_is_disabled_in_value(eax);
    pal_get_leaf_0d_eax_subleaf_0_mpx_state_at_index(1);
    pal_get_leaf_0d_eax_subleaf_0_mpx_state_from_value(eax);

    // Printers
    pal_print_leaf_0d_eax_subleaf_0_at_index(printf, 1);
    pal_print_leaf_0d_eax_subleaf_0_from_value(printf, eax);
    pal_print_leaf_0d_eax_subleaf_0_sse_state_at_index(printf, 1);
    pal_print_leaf_0d_eax_subleaf_0_sse_state_from_value(printf, eax);
    pal_print_leaf_0d_eax_subleaf_0_mpx_state_at_index(printf, 1);
    pal_print_leaf_0d_eax_subleaf_0_mpx_state_from_value(printf, eax);
}
