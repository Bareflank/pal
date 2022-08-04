#include <iostream>

// Either include a header file for an instruction you want to execute...
#include "pal/instruction/rdmsr.h"
#include "pal/instruction/cpuid.h"

// ... or for a register you want to interact with by name
#include "pal/msr/efer.h"
#include "pal/msr/tsc.h"
#include "pal/cpuid/largfuncnum.h"
#include "pal/cpuid/fammodstep.h"
#include "pal/cpuid/featureidebx.h"
#include "pal/cpuid/featureidecx.h"
#include "pal/cpuid/featureidedx.h"
#include "pal/control_register/cr0.h"

// PAL can also pretty-print things for you through any printf-like function:
#include <stdio.h>

int main(void)
{
    // For C++11 everything in PAL is contained in the "pal" namespace
    using namespace pal;

    // PAL lets you interact with instructions and registers using their name
    // as defined by a reference manual. For example, read the EFER MSR, and
    // then print its value:
    auto efer_value = efer::get();
    efer::print(printf, efer_value);

    // As another example, read the TSC MSR using its address as an input to the
    // RDMSR instruction
    auto tsc_value = execute_rdmsr(tsc::address);
    tsc::print(printf, tsc_value);

    // You can also print register contents without storing the value in a
    // variable. For example, print part of a CPUID leaf:
    largfuncnum::print(printf);

    // In C++11, instructions that logically output more than one value are
    // returned by PAL as tuples for easy integration with std::tie:
    uint32_t eax{0};
    uint32_t ebx{0};
    uint32_t ecx{0};
    uint32_t edx{0};
    std::tie(eax, ebx, ecx, edx) = execute_cpuid(fammodstep::function, 0);
    fammodstep::print(printf, eax);
    featureidebx::print(printf, ebx);
    featureidecx::print(printf, ecx);
    featureidedx::print(printf, edx);

    // Registers that contain named fields can also be accessed by name.
    // For example, check if paging is enabled by reading the PG bit in control 
    // register CR0
    if(cr0::pg::is_enabled()) {
        std::cout << "Paging is enabled" << std::endl;
    }
}
