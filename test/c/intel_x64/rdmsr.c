#include <pal/instruction/rdmsr.h>
#include <pal/msr/ia32_feature_control.h>

void test_rdmsr_compile(void)
{
    uint32_t address = PAL_IA32_FEATURE_CONTROL_ADDRESS;
    uint64_t value = pal_execute_rdmsr(address);
    pal_print_ia32_feature_control_from_value(value);
}
