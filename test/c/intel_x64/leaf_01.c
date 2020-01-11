#include <pal/cpuid/leaf_01_eax.h>
#include <pal/cpuid/leaf_01_ebx.h>
#include <pal/cpuid/leaf_01_ecx.h>
#include <pal/cpuid/leaf_01_edx.h>

void test_leaf_01_compile(void)
{
    // Register accessors
    uint32_t eax = pal_leaf_01_eax_get();
    uint32_t ebx = pal_leaf_01_ebx_get();
    uint32_t ecx = pal_leaf_01_ecx_get();
    uint32_t edx = pal_leaf_01_edx_get();

    // Field accessors
    pal_leaf_01_eax_model_get();
    pal_leaf_01_eax_model_get_from_value(eax);

    // Printers
    pal_leaf_01_eax_dump();
    pal_leaf_01_eax_dump_from_value(eax);
    pal_leaf_01_eax_model_dump();
    pal_leaf_01_eax_model_dump_from_value(eax);
}
