#include <pal/instruction/read_cr0.h>

void test_read_cr0_compile(void)
{
    uint64_t value = pal_execute_read_cr0();
}
