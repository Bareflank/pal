#include <pal/cpuid/leaf_04_eax.h>
#include <pal/cpuid/leaf_04_ebx.h>
#include <pal/cpuid/leaf_04_ecx.h>
#include <pal/cpuid/leaf_04_edx.h>
#include <stdio.h>

void test_leaf_04_compile(void)
{
    // Register accessors
    uint32_t eax = pal_get_leaf_04_eax_at_index(1);
    uint32_t ebx = pal_get_leaf_04_ebx_at_index(1);
    uint32_t ecx = pal_get_leaf_04_ecx_at_index(1);
    uint32_t edx = pal_get_leaf_04_edx_at_index(1);

    // Field accessors
    pal_leaf_04_eax_self_initializing_cache_level_is_enabled_at_index(1);
    pal_leaf_04_eax_self_initializing_cache_level_is_enabled_in_value(eax);
    pal_leaf_04_eax_self_initializing_cache_level_is_disabled_at_index(1);
    pal_leaf_04_eax_self_initializing_cache_level_is_disabled_in_value(eax);
    pal_get_leaf_04_eax_cache_type_at_index(1);
    pal_get_leaf_04_eax_cache_type_from_value(eax);

    // Printers
    pal_print_leaf_04_eax_at_index(printf, 1);
    pal_print_leaf_04_eax_from_value(printf, eax);
    pal_print_leaf_04_eax_self_initializing_cache_level_at_index(printf, 1);
    pal_print_leaf_04_eax_self_initializing_cache_level_from_value(printf, eax);
    pal_print_leaf_04_eax_cache_type_at_index(printf, 1);
    pal_print_leaf_04_eax_cache_type_from_value(printf, eax);
}
