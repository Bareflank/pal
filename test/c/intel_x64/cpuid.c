#include <pal/instruction/cpuid.h>
#include <pal/cpuid/leaf_01_eax.h>

void test_cpuid_compile(void)
{
    uint32_t leaf = 0x1;
    uint32_t subleaf = 0x0;

    pal_cpuid_return_values output = pal_execute_cpuid(leaf, subleaf);

    uint32_t eax = output.eax;
    uint32_t ebx = output.ebx;
    uint32_t ecx = output.ecx;
    uint32_t edx = output.edx;

    pal_print_leaf_01_eax_from_value(eax);
    uint32_t family_id = pal_get_leaf_01_eax_family_id_from_value(eax);
}
