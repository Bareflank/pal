#include <pal/cpuid/leaf_04_eax.h>
#include <pal/cpuid/leaf_04_ebx.h>
#include <pal/cpuid/leaf_04_ecx.h>
#include <pal/cpuid/leaf_04_edx.h>

void test_leaf_04_compile(void)
{
    // Register accessors
    auto eax = pal::leaf_04_eax::get_at_index(1);
    auto ebx = pal::leaf_04_ebx::get_at_index(1);
    auto ecx = pal::leaf_04_ecx::get_at_index(1);
    auto edx = pal::leaf_04_edx::get_at_index(1);

    // Field accessors
    pal::leaf_04_eax::self_initializing_cache_level::is_enabled_at_index(1);
    pal::leaf_04_eax::self_initializing_cache_level::is_enabled(eax);
    pal::leaf_04_eax::self_initializing_cache_level::is_disabled_at_index(1);
    pal::leaf_04_eax::self_initializing_cache_level::is_disabled(eax);
    pal::leaf_04_eax::cache_type::get_at_index(1);
    pal::leaf_04_eax::cache_type::get(eax);

    // Printers
    pal::leaf_04_eax::print_at_index(1);
    pal::leaf_04_eax::print(eax);
    pal::leaf_04_eax::self_initializing_cache_level::print_at_index(1);
    pal::leaf_04_eax::self_initializing_cache_level::print(eax);
    pal::leaf_04_eax::cache_type::print_at_index(1);
    pal::leaf_04_eax::cache_type::print(eax);
}
