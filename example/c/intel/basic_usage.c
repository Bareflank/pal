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

// PAL can also pretty-print things for you through any printf-like function:
#include <stdio.h>

int main(void)
{
    // PAL lets you interact with instructions and registers using their name
    // as defined by a reference manual. For example, read the
    // IA32_FEATURE_CONTROL MSR, and then print its value:
    uint64_t msr_value = pal_get_ia32_feature_control();
    pal_print_ia32_feature_control_from_value(printf, msr_value);

    // As another example, read the IA32_TSC MSR using its address as an input
    // to the x86 RDMSR instruction
    uint32_t address = PAL_IA32_TSC_ADDRESS;
    uint64_t msr_value_2 = pal_execute_rdmsr(address);

    // You can also print register contents without storing the value in a
    // variable. For example, print part of a CPUID leaf:
    pal_print_leaf_01_eax(printf);

    // In C, instructions that logically output more than one value are returned
    // by PAL as structs, typedef'ed for convinience:
    pal_cpuid_return_values cpuid_outputs = pal_execute_cpuid(2, 0);
    pal_print_leaf_02_eax_from_value(printf, cpuid_outputs.eax);
    pal_print_leaf_02_ebx_from_value(printf, cpuid_outputs.ebx);
    pal_print_leaf_02_ecx_from_value(printf, cpuid_outputs.ecx);
    pal_print_leaf_02_edx_from_value(printf, cpuid_outputs.edx);

    // Registers that contain named fields can also be accessed by name.
    // For example, check if paging is enabled by reading the PG bit in control
    // register CR0
    if(pal_cr0_pg_is_enabled()) {
        printf("Paging is enabled\n");
    }
}

