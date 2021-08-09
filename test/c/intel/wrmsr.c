#include <pal/instruction/wrmsr.h>

void test_wrmsr_compile(void)
{
    pal_execute_wrmsr(0xBADC0FFE, 0xDEADBEEF);
}
