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
    // PAL lets you interact with instructions and registers using their name
    // as defined by a reference manual. For example, read the EFER MSR, and
    // then print its value:
    uint64_t efer_value = pal_get_efer();
    pal_print_efer_from_value(printf, efer_value);

    // As another example, read the TSC MSR using its address as an input to the
    // RDMSR instruction
    uint64_t tsc_value = pal_execute_rdmsr(PAL_TSC_ADDRESS);
    pal_print_tsc_from_value(printf, tsc_value);

    // You can also print register contents without storing the value in a
    // variable. For example, print part of a CPUID leaf:
    pal_print_largfuncnum(printf);

    // In C++11, instructions that logically output more than one value are
    // returned by PAL as tuples for easy integration with std::tie:
    pal_cpuid_return_values cpuid_outputs = pal_execute_cpuid(PAL_FAMMODSTEP_FUNCTION, 0);
    pal_print_fammodstep_from_value(printf, cpuid_outputs.eax);
    pal_print_featureidebx_from_value(printf, cpuid_outputs.ebx);
    pal_print_featureidecx_from_value(printf, cpuid_outputs.ecx);
    pal_print_featureidedx_from_value(printf, cpuid_outputs.edx);

    // Registers that contain named fields can also be accessed by name.
    // For example, check if paging is enabled by reading the PG bit in control 
    // register CR0
    if(pal_cr0_pg_is_enabled()) {
        printf("Paging is enabled\n");
    }
}
