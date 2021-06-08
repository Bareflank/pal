#include <iostream>

// Either include a header file for an instruction you want to execute...
#include "pal/instruction/rdmsr.h"
#include "pal/instruction/cpuid.h"

// ... or for a register you want to interact with by name
#include "pal/msr/ia32_feature_control.h"
#include "pal/msr/ia32_tsc.h"
#include "pal/cpuid/leaf_01_eax.h"
#include "pal/cpuid/leaf_02_eax.h"
#include "pal/cpuid/leaf_02_ebx.h"
#include "pal/cpuid/leaf_02_ecx.h"
#include "pal/cpuid/leaf_02_edx.h"
#include "pal/control_register/cr0.h"

int main()
{
    // For C++11 everything in PAL is contained in the "pal" namespace
    using namespace pal;

    // PAL lets you interact with instructions and registers using their name
    // as defined by a reference manual. For example, read the
    // IA32_FEATURE_CONTROL MSR, and then print its value:
    auto msr_value = ia32_feature_control::get();
    ia32_feature_control::print(msr_value);

    // As another example, read the IA32_TSC MSR using its address as an input
    // to the x86 RDMSR instruction
    auto address = ia32_tsc::address;
    auto msr_value_2 = execute_rdmsr(address);

    // You can also print register contents without storing the value in a
    // variable. For example, print part of a CPUID leaf:
    leaf_01_eax::print();

    // In C++11, instructions that logically output more than one value are
    // returned by PAL as tuples for easy integration with std::tie:
    uint32_t eax{0};
    uint32_t ebx{0};
    uint32_t ecx{0};
    uint32_t edx{0};
    std::tie(eax, ebx, ecx, edx) = execute_cpuid(2, 0);
    leaf_02_eax::print(eax);
    leaf_02_ebx::print(ebx);
    leaf_02_ecx::print(ecx);
    leaf_02_edx::print(edx);

    // Registers that contain named fields can also be accessed by name.
    // For example, check if paging is enabled by reading the PG bit in control 
    // register CR0
    if(cr0::pg::is_enabled()) {
        std::cout << "Paging is enabled" << std::endl;
    }
}
