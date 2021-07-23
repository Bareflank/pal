#include <pal/cpuid/leaf_01_eax.h>
#include <pal/cpuid/leaf_01_ebx.h>
#include <pal/cpuid/leaf_01_ecx.h>
#include <pal/cpuid/leaf_01_edx.h>
#include <stdio.h>

void test_leaf_01_compile(void)
{
    // Register accessors
    uint32_t eax = pal_get_leaf_01_eax();
    uint32_t ebx = pal_get_leaf_01_ebx();
    uint32_t ecx = pal_get_leaf_01_ecx();
    uint32_t edx = pal_get_leaf_01_edx();

    // Field accessors
    pal_get_leaf_01_eax_model();
    pal_get_leaf_01_eax_model_from_value(eax);

    // Printers
    pal_print_leaf_01_eax(printf);
    pal_print_leaf_01_eax_from_value(printf, eax);
    pal_print_leaf_01_eax_model(printf);
    pal_print_leaf_01_eax_model_from_value(printf, eax);
}
