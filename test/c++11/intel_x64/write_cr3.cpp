#include <pal/instruction/write_cr3.h>

void test_write_cr3_compile(void)
{
    pal::execute_write_cr3(0xDEADBEEF);
}
