#include <pal/cpuid/leaf_0d_eax.h>
#include <pal/cpuid/leaf_0d_ebx.h>
#include <pal/cpuid/leaf_0d_ecx.h>
#include <pal/cpuid/leaf_0d_edx.h>

void test_leaf_0d_compile(void)
{
    // Register accessors
    uint32_t eax = pal_leaf_0d_eax_get_at_index(1);
    uint32_t ebx = pal_leaf_0d_ebx_get_at_index(1);
    uint32_t ecx = pal_leaf_0d_ecx_get_at_index(1);
    uint32_t edx = pal_leaf_0d_edx_get_at_index(1);

    // Field accessors
    pal_leaf_0d_eax_subleaf_0_sse_state_is_enabled_at_index(1);
    pal_leaf_0d_eax_subleaf_0_sse_state_is_enabled_from_value(eax);
    pal_leaf_0d_eax_subleaf_0_sse_state_is_disabled_at_index(1);
    pal_leaf_0d_eax_subleaf_0_sse_state_is_disabled_from_value(eax);
    pal_leaf_0d_eax_subleaf_0_mpx_state_get_at_index(1);
    pal_leaf_0d_eax_subleaf_0_mpx_state_get_from_value(eax);

    // Printers
    pal_leaf_0d_eax_subleaf_0_dump_at_index(1);
    pal_leaf_0d_eax_subleaf_0_dump_from_value(eax);
    pal_leaf_0d_eax_subleaf_0_sse_state_dump_at_index(1);
    pal_leaf_0d_eax_subleaf_0_sse_state_dump_from_value(eax);
    pal_leaf_0d_eax_subleaf_0_mpx_state_dump_at_index(1);
    pal_leaf_0d_eax_subleaf_0_mpx_state_dump_from_value(eax);
}
