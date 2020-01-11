#include <pal/cpuid/leaf_01_eax.h>
#include <pal/cpuid/leaf_01_ebx.h>
#include <pal/cpuid/leaf_01_ecx.h>
#include <pal/cpuid/leaf_01_edx.h>

void test_leaf_01_compile(void)
{
    // Register accessors
    auto eax = pal::leaf_01_eax::get();
    auto ebx = pal::leaf_01_ebx::get();
    auto ecx = pal::leaf_01_ecx::get();
    auto edx = pal::leaf_01_edx::get();

    // Field accessors
    pal::leaf_01_eax::model::get();
    pal::leaf_01_eax::model::get(eax);

    // Printers
    pal::leaf_01_eax::dump();
    pal::leaf_01_eax::dump(eax);
    pal::leaf_01_eax::model::dump();
    pal::leaf_01_eax::model::dump(eax);
}
