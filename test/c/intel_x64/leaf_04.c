#include <pal/cpuid/leaf_04_eax.h>
#include <pal/cpuid/leaf_04_ebx.h>
#include <pal/cpuid/leaf_04_ecx.h>
#include <pal/cpuid/leaf_04_edx.h>

void test_leaf_04_compile(void)
{
    // Register accessors
    uint32_t eax = pal_leaf_04_eax_get_at_index(1);
    uint32_t ebx = pal_leaf_04_ebx_get_at_index(1);
    uint32_t ecx = pal_leaf_04_ecx_get_at_index(1);
    uint32_t edx = pal_leaf_04_edx_get_at_index(1);

    // Field accessors
    pal_leaf_04_eax_self_initializing_cache_level_is_enabled_at_index(1);
    pal_leaf_04_eax_self_initializing_cache_level_is_enabled_from_value(eax);
    pal_leaf_04_eax_self_initializing_cache_level_is_disabled_at_index(1);
    pal_leaf_04_eax_self_initializing_cache_level_is_disabled_from_value(eax);
    pal_leaf_04_eax_cache_type_get_at_index(1);
    pal_leaf_04_eax_cache_type_get_from_value(eax);

    // Printers
    pal_leaf_04_eax_dump_at_index(1);
    pal_leaf_04_eax_dump_from_value(eax);
    pal_leaf_04_eax_self_initializing_cache_level_dump_at_index(1);
    pal_leaf_04_eax_self_initializing_cache_level_dump_from_value(eax);
    pal_leaf_04_eax_cache_type_dump_at_index(1);
    pal_leaf_04_eax_cache_type_dump_from_value(eax);
}
