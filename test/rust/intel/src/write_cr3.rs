use pal;

pub unsafe fn test_write_cr3_compile()
{
    pal::instruction::execute_write_cr3(0xDEADBEEF);
}
