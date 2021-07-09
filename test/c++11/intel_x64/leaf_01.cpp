#include <pal/cpuid/leaf_01_eax.h>
#include <pal/cpuid/leaf_01_ebx.h>
#include <pal/cpuid/leaf_01_ecx.h>
#include <pal/cpuid/leaf_01_edx.h>
#include <stdio.h>

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
    pal::leaf_01_eax::print(printf);
    pal::leaf_01_eax::print(printf, eax);
    pal::leaf_01_eax::model::print(printf);
    pal::leaf_01_eax::model::print(printf, eax);
}
