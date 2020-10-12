int main(int argc, char * argv[])
{ }

extern "C"
{

void _start(void)
{ main(0, 0);}

int putchar(int c)
{ return 0; }

int __printf_chk(int flag, const char * format, ...)
{ return 0; }

void __aeabi_unwind_cpp_pr0(void)
{}

void __aeabi_unwind_cpp_pr1(void)
{}

void __stack_chk_guard(void)
{}

void __stack_chk_fail(void)
{}

int printf ( const char * format, ... )
{ return 0; }

}
