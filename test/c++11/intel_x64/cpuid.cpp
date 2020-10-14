#include <pal/instruction/cpuid.h>
#include <pal/cpuid/leaf_01_eax.h>

void test_cpuid_compile(void)
{
    // Inputs
    uint32_t leaf{0x1};
    uint32_t subleaf{0x0};

    // Outputs
    uint32_t eax{0};
    uint32_t ebx{0};
    uint32_t ecx{0};
    uint32_t edx{0};

    std::tie(eax, ebx, ecx, edx) = pal::execute_cpuid(leaf, subleaf);

    pal::leaf_01_eax::print(eax);
    uint32_t family_id = pal::leaf_01_eax::family_id::get(eax);
}
