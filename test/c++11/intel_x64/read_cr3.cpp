#include <pal/instruction/read_cr3.h>

void test_read_cr3_compile(void)
{
    uint64_t value = pal::execute_read_cr3();
}
